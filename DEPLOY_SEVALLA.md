# تنصيب البوت على Sevalla

## 1. الملفات المضافة
تم إضافة:
- `Dockerfile` — لبناء البوت كصورة Docker (يثبت ffmpeg تلقائيًا)
- `requirements.txt` — نسخة من `r3d.txt`
- `.env.example` — قائمة بالمتغيرات المطلوبة
- تعديل `main.py` و `clean.py` ليعملا بمتغيرات البيئة بدل الإدخال اليدوي (input)، لأن Sevalla لا توفر Terminal تفاعلي عند التشغيل

## 2. ارفع المشروع على GitHub
Sevalla يبني التطبيق من مستودع Git (أو من Docker image مباشرة). ارفع هذا المجلد كمستودع.

## 3. أنشئ قاعدة بيانات Redis
من لوحة Sevalla: **Databases → Add Database → Redis**
بعد الإنشاء، انسخ رابط الاتصال الداخلي (Internal Connection String) — سيكون بالشكل:
`redis://default:password@host:port`

## 4. أنشئ التطبيق (Application)
- **Application Hosting → Add Application**
- اربطه بمستودع الكود
- **Build method**: اختر **Dockerfile** (موجود جاهز في المشروع)
- **Process type**: اختره كـ **Background Worker** وليس Web Service — لأن هذا بوت تيليجرام ولا يحتاج منفذ HTTP

## 5. أضف متغيرات البيئة (Environment Variables)
في إعدادات التطبيق أضف:

| المتغير | القيمة |
|---|---|
| `API_ID` | من https://my.telegram.org |
| `API_HASH` | من https://my.telegram.org |
| `TOKEN` | التوكن من @BotFather |
| `SUDO_ID` | آيدي حسابك على تيليجرام (رقمي) |
| `REDIS_URL` | رابط Redis الذي نسخته في الخطوة 3 |

## 6. Deploy
اضغط Deploy. البوت سينشئ ملف `config.py` تلقائيًا عند كل تشغيل بالاعتماد على متغيرات البيئة، ثم يبدأ التشغيل مباشرة (بدون أي إدخال يدوي).

## ملاحظات
- الحاوية (container) على Sevalla لا تحتفظ بالملفات بين عمليات إعادة النشر، لذا أي بيانات مهمة يجب تخزينها في Redis وليس بملفات محلية (مثل `ytdb.sqlite` التي ينشئها kvsqlite) — إذا احتجت تخزينًا دائمًا لهذه الملفات اسأل عن إضافة Persistent Storage أو Object Storage من Sevalla.
- تأكد أن جميع البلوغنز (Plugins) لا تحتوي على مسارات مطلقة محلية قد تختفي بعد إعادة التشغيل.
