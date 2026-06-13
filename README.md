# موديول مستخلصات المقاولين الذكي لجاري وسابق - أودو 19 (Odoo 19 Module)

هذا هو الكود المصدري الكامل والمطور خصيصاً للتوافق والمطابقة بنسبة 100% مع حسابات مستخلصات المقاولين والمباني السكنية والتجارية، مع دعم كامل للغة العربية.

---

## 📌 ميزات الموديول (Key Features):
1. **طريقتين للحساب (Calculation Methods):**
   * **الحساب التراكمي العام (Standard Cumulative):** يطرح ما صرف سابقاً بشكل مقاصة متراكمة.
   * **التسوية الحالية المباشرة (Direct Jari Method):** مطابق لحسابات مستخلص جاري 7 بالصورة، حيث تخصم الدفع الدورية وضمان الأعمال والذمم والضريبة مباشرة من دفعة المنجز الحالي.
2. **شجرة حسابات ورقية وذكية (BOQ Grid):** جدول بملخص بنود الأعمال والكميات المنفذة (سابق، حالي، تراكمي الفئة).
3. **التصميم المعتمد والمطبوع (Arabic Custom Print Report):** تقرير طباعة Qweb PDF فاخر مع تذييل التوقيعات للاعتماد الفني والمالي.
4. **شريط سير العمل والاعتماد (Workflows):** (مسودة -> مراجعة الاستشاري والتدقيق -> اعتماد ومطابقة -> تأكيد الصرف).

---

## 🚀 كيفية التثبيت على نظام أودو أونلاين نسخة 19 (How to Install on Odoo Online):

> ⚠️ **تنبيه هام حول شروط أودو أونلاين (Odoo Online Custom Modules Policy):**
> * إذا كانت باقتك هي **أودو أونلاين القياسية (SaaS Standard)**، فإن أودو لا تسمح برفع ملفات برمجية مخصصة (Custom Python Code) بشكل مباشر.
> * لتثبيت هذا الموديول المخصص، يتوجب عليك استخدام **مشروع Odoo.sh** كبيئة تشغيل سحابية (وهو مدعوم بالكامل ومثالي)، أو نقل قاعدة البيانات إلى استضافة **أودو على خادم خاص (Self-Hosted/On-Premise)**.

### طريقة الرفع على Odoo.sh:
1. قم بإنشاء مستودع (Repository) خاص بك على غيت هاب (GitHub).
2. انسخ مجلد الموديول الحالي `odoo_mostakhlas_module` وضعه بداخل مستودعك.
3. اربط مستودع GitHub مع مشروعك على **Odoo.sh**.
4. سيقوم أودو بفحص الموديول وتثبيته تلقائياً على نسخة Odoo Online 19 الخاصة بك!
5. توجه نحو الإعدادات في أودو، وقم بتفعيل **نمط المطور (Developer Mode)**.
6. اذهب إلى قائمة **التطبيقات (Apps)** -> اضغط على **تحديث قائمة التطبيقات (Update Apps List)** -> ابحث عن `Rawat Mostakhlas Billing` واضغط **تثبيت (Install)**.

---

## 🛠️ البديل لنسخة أودو أونلاين القياسية باستخدام API:
إذا لم تكن مشتركاً بـ Odoo.sh وتود مزامنة البيانات مباشرة من هذا التطبيق (React Portal) إلى أودو أونلاين، يمكنك استخدام **واجهة برمجة تطبيقات أودو (Odoo External API via XML-RPC)** لإنشاء فواتير المشتريات (Vendor Bills) مباشرة في المديول الافتراضي `account.move`:

```python
# كود بايثون تقريبي للمزامنة عبر API بدون موديولات مخصصة
import xmlrpc.client

url = "https://your-database.odoo.com"
db = "your-db-name"
username = "your-email"
password = "your-api-key"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# إنشاء فاتورة مستخلص في أودو تلقائياً
invoice_id = models.execute_kw(db, uid, password, 'account.move', 'create', [{
    'move_type': 'in_invoice', # فاتورة مورد/مقاول
    'partner_id': contractor_partner_id,
    'ref': 'مستخلص جاري رقم 7 - روعة عالم التصميم',
    'invoice_date': '2026-06-11',
    'invoice_line_ids': [
        (0, 0, {
            'name': 'بند خرسانات وأعمال إنشائية جاري 7',
            'quantity': 1,
            'price_unit': 2732791.60, # قيمة المنجز الحالي
        })
    ]
}])
```
