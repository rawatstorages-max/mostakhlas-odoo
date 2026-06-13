# -*- coding: utf-8 -*-
{
    'name': 'Rawat Mostakhlas Billing (Odoo 19)',
    'version': '1.0',
    'summary': 'ادارة مستخلصات المقاولين والأعمال الإنشائية بالتسوية التراكمية والمباشرة',
    'description': """
مستخلصات المقاولين الذكية - شركة روعة عالم التصميم
===================================================
هذا المديول يضيف نظام إدارة مستخلصات المقاولين الكامل لنسخة أودو 19:
* تسجيل وحساب بنود مستخلصات جاري (سواء الطريقة التراكمية أو المباشرة جاري 7).
* خصم الدفع المقدمة المباشرة وضمان الأعمال (توقيفات الإنجاز) من المستخلص.
* حساب ضريبة القيمة المضافة ومستحقات المقاولين بشكل آلي.
* توليد مستند طباعة عربي رسمي معتمد (تقرير QWeb).
* يدعم التكامل مع موديولات المشاريع والحسابات العامة في أودو.
""",
    'author': 'Rawat Smart Contracting & AI Studio',
    'category': 'Project/Accounting',
    'depends': ['base', 'account', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/mostakhlas_views.xml',
        'report/mostakhlas_report_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
