# منصة تحويل النص إلى صوت احترافي باللغة العربية

## المتطلبات

- Python 3.7+
- حساب Google Cloud مفعّل فيه Text-to-Speech API
- إعداد متغير البيئة GOOGLE_APPLICATION_CREDENTIALS ليشير إلى ملف الخدمة

## التشغيل

```bash
pip install -r requirements.txt
python app.py
```

## الاستخدام

- افتح المتصفح على [http://localhost:5000](http://localhost:5000)
- أدخل النص، اختر الصوت، اضبط السرعة والنبرة، واضغط "تحويل إلى صوت".

## ملاحظات:
- يجب أن يكون لديك ملف خدمة Google Cloud (json) وقمت بضبط متغير البيئة:
  ```
  export GOOGLE_APPLICATION_CREDENTIALS="YOUR_PATH_TO_SERVICE_KEY.json"
  ```
- لمزيد من النماذج الصوتية أو اللهجات، راجع [توثيق Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/voices).