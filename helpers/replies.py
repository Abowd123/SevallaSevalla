# -*- coding: utf-8 -*-
# Reply customization engine (Phase 1/2)
# t() is SYNC and only tags the text; override lookup + formatting happen at send
# time inside the patched Message methods (which can await Redis).
import logging
from config import *
from pyrogram.types import *


class TaggedStr(str):
    """A normal string carrying the reply key + default template + args."""
    pass


def t(key, default, *args):
    """Return a tagged reply string; falls back to the default template now,
    override resolution is applied later at send time."""
    if args:
        try:
            base = default.format(*args)
        except Exception:
            base = default
    else:
        base = default
    s = TaggedStr(base)
    s._rkey = key
    s._rdefault = default
    s._rargs = args
    return s


async def _resolve(chat_id, text):
    key = getattr(text, "_rkey", None)
    default = getattr(text, "_rdefault", str(text))
    fargs = getattr(text, "_rargs", ())
    override = None
    try:
        if chat_id is not None:
            override = await r.get(f"ro:{chat_id}:{key}")
        if not override:
            override = await r.get(f"ro:g:{Dev_Zaid}:{key}")
    except Exception as e:
        logging.exception(e)
        override = None
    tmpl = override if override else default
    if not fargs:
        return tmpl
    try:
        return tmpl.format(*fargs)
    except Exception:
        try:
            return default.format(*fargs)
        except Exception:
            return str(text)


async def _wrap(orig, self, *args, **kwargs):
    text = args[0] if args else kwargs.get("text")
    key = getattr(text, "_rkey", None)
    if key is not None:
        try:
            chat_id = getattr(getattr(self, "chat", None), "id", None)
            resolved = await _resolve(chat_id, text)
            if args:
                args = (resolved,) + tuple(args[1:])
            else:
                kwargs["text"] = resolved
        except Exception as e:
            logging.exception(e)
    msg = await orig(self, *args, **kwargs)
    if key is not None:
        try:
            mid = getattr(msg, "id", None)
            cid = getattr(getattr(msg, "chat", None), "id", None)
            if mid is not None and cid is not None:
                await r.set(f"rk:{cid}:{mid}", key, ex=604800)
        except Exception as e:
            logging.exception(e)
    return msg


def install():
    """Idempotently patch Message send methods so tagged replies resolve overrides.
    For non-tagged text this is a pure pass-through (behavior unchanged)."""
    if getattr(Message, "_rpatched", False):
        return
    for name in ("reply_text", "reply", "edit_text", "edit_message_text"):
        orig = getattr(Message, name, None)
        if orig is None:
            continue

        def make(orig):
            async def patched(self, *args, **kwargs):
                return await _wrap(orig, self, *args, **kwargs)
            return patched

        setattr(Message, name, make(orig))
    Message._rpatched = True


async def set_override(chat_id, key, value, glob=False):
    if glob:
        await r.set(f"ro:g:{Dev_Zaid}:{key}", value)
    else:
        await r.set(f"ro:{chat_id}:{key}", value)


async def clear_override(chat_id, key, glob=False):
    if glob:
        await r.delete(f"ro:g:{Dev_Zaid}:{key}")
    else:
        await r.delete(f"ro:{chat_id}:{key}")


async def get_key_for_message(chat_id, msg_id):
    try:
        return await r.get(f"rk:{chat_id}:{msg_id}")
    except Exception as e:
        logging.exception(e)
        return None


async def set_label(key, label):
    """Store a human-readable label (what the reply used to look like) for listing."""
    try:
        await r.set(f"rl:g:{Dev_Zaid}:{key}", label)
    except Exception as e:
        logging.exception(e)


async def list_overrides(limit=80):
    """Return list of (key, label, value) for all global reply overrides."""
    out = []
    prefix = f"ro:g:{Dev_Zaid}:"
    try:
        async for k in r.scan_iter(match=prefix + "*", count=200):
            key = k[len(prefix):]
            val = await r.get(k)
            lbl = await r.get(f"rl:g:{Dev_Zaid}:{key}")
            out.append((key, lbl, val))
            if len(out) >= limit:
                break
    except Exception as e:
        logging.exception(e)
    return out


async def clear_all_overrides():
    """Delete all global reply overrides (and their labels). Returns count."""
    n = 0
    prefix = f"ro:g:{Dev_Zaid}:"
    try:
        keys = []
        async for k in r.scan_iter(match=prefix + "*", count=200):
            keys.append(k)
        for k in keys:
            key = k[len(prefix):]
            await r.delete(k)
            await r.delete(f"rl:g:{Dev_Zaid}:{key}")
            n += 1
    except Exception as e:
        logging.exception(e)
    return n
