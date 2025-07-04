# -*- coding: utf-8 -*-
{
    'name': "BI Survey Template",

    'summary': "This template is for Surveys Module Bank Indonesia",

    'description': """
This template is customization in Surveys Module for Bank Indonesia
    """,

    'author': "PT. Lintang Utama Infotek",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/survey_templates.xml',
        'views/survey_templates_statistic.xml',
    ],
    'application': False,
    'installable': True,
}

