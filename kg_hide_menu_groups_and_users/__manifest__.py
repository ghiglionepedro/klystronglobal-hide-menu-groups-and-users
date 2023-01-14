# -*- coding: utf-8 -*-

# Klystron Global LLC
# Copyright (C) Klystron Global LLC
# All Rights Reserved
# https://www.klystronglobal.com/


{
    'name': "hide menu groups and users",
    'summary': """
        Restrict Menu Items from Specific Users and groups""",
    'description': """
        Restrict Menu Items from Specific Users and groups""",
    'author': 'core: Klystron Global. Extend: Ghiglione Pedro Matias',
    'maintainer':'Kiran K',
    'website': "https://www.klystronglobal.com/",
    'images': ["static/description/banner.png"],
    'category': 'Extra Rights',
    'version': "15.0.1.0.0",
    'license': 'AGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'views/res_users.xml',
        'views/res_groups.xml',
             ],
}
