FROM python:3.11-slim

# System deps: ffmpeg is required by the downloader/voice plugins
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# This is a background worker (Telegram bot), not a web server — no EXPOSE/port needed.
CMD ["python3", "main.py"]
