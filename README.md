# rawafid-fintech <div align="center">

<img src="https://img.shields.io/badge/روافد_فنتك-2026-gold?style=for-the-badge&labelColor=1a1a2e" alt="Rawafid Fintech 2026"/>

# 🏦 Rawafid Fintech — روافد فنتك

### معرض رواد الفنتك في المملكة العربية السعودية

[![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Arabic RTL](https://img.shields.io/badge/Arabic-RTL-green?style=flat-square&logo=googletranslate&logoColor=white)](https://en.wikipedia.org/wiki/Right-to-left)
[![Static Site](https://img.shields.io/badge/Static-Site-blue?style=flat-square&logo=github-pages&logoColor=white)](https://pages.github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

-----

## 📌 نبذة عن المشروع

**روافد فنتك** هو معرض تجاري متخصص في قطاع التقنية المالية (Fintech) في المملكة العربية السعودية، يُقام في **جامعة الإمام محمد بن سعود الإسلامية، الرياض** خلال الفترة **5–6 مايو 2026**.

الصفحة مصممة بالكامل باللغة العربية (RTL) وتستهدف الشركات الراغبة في الرعاية والمشاركة في المعرض.

-----

## ✨ المميزات

- 🕌 **واجهة عربية بالكامل** — تصميم RTL احترافي
- 🎨 **تصميم أنيق** — خطوط Cairo & Tajawal من Google Fonts
- ⚡ **بدون dependencies** — ملف HTML واحد يحتوي كل شيء
- 📱 **متجاوب** — يعمل على الجوال والكمبيوتر
- 🖨️ **دعم PDF** — تصدير ملصقات وكتيبات الرعاية

-----

## 🗂️ هيكل المشروع

```
rawafid-fintech/
├── 📄 index.html          # الصفحة الرئيسية (883 سطر، كل شيء فيها)
├── 📄 index_mini.html     # نسخة مختصرة
├── 🖼️ poster.html         # ملصق المعرض
├── 🖼️ poster2/3.html      # نسخ بديلة للملصق
├── 🖼️ poster_ig.html      # ملصق انستقرام
├── 🖼️ poster_canva.html   # نسخة Canva
├── 🐍 server.py           # سيرفر Python بسيط
├── 🐍 make_pdf.py         # تصدير PDF
├── 🐍 make_poster.py      # توليد الملصقات
├── 🖼️ logo.png            # شعار روافد
└── 🎨 NotoSansArabic.ttf  # خط عربي للطباعة
```

-----

## 🚀 تشغيل المشروع

> لا يحتاج أي تثبيت أو build system — فقط Python!

```bash
# استنسخ المشروع
git clone https://github.com/Mjeed19/rawafid-fintech.git
cd rawafid-fintech

# شغّل السيرفر
python3 -m http.server 5000
```

ثم افتح المتصفح على:

```
http://localhost:5000
```

-----

## 🖨️ تصدير PDF

```bash
python3 make_pdf.py
```

-----

## 🛠️ التقنيات المستخدمة

|التقنية                        |الاستخدام            |
|-------------------------------|---------------------|
|`HTML5 / CSS3 / JS`            |الصفحة الرئيسية كاملة|
|`Python 3`                     |سيرفر محلي وتصدير PDF|
|`Google Fonts (Cairo, Tajawal)`|الخطوط العربية       |
|`RTL Layout`                   |دعم اللغة العربية    |

-----

## 📍 تفاصيل الفعالية

|التفصيل  |المعلومة                         |
|---------|---------------------------------|
|📅 التاريخ|5–6 مايو 2026                    |
|📍 المكان |جامعة الإمام محمد بن سعود، الرياض|
|🎯 الجمهور|شركات الفنتك والرعاة في السعودية |
|🌐 اللغة  |عربي                             |

-----

## 🤝 المساهمة

المساهمات مرحب بها! افتح **Issue** أو أرسل **Pull Request**.

-----

<div align="center">

صُنع بـ ❤️ في المملكة العربية السعودية 🇸🇦

</div>
