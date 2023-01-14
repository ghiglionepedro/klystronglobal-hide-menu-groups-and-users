# -*- coding: utf-8 -*-

# Klystron Global LLC
# Copyright (C) Klystron Global LLC
# All Rights Reserved
# https://www.klystronglobal.com/


from odoo import fields, models, api


class ResGroups(models.Model):
    _inherit = 'res.groups'

    hide_group_menu_access_ids = fields.Many2many('ir.ui.menu', 'ir_ui_hide_menu_group_rel', 'uid', 'menu_id',
                                            string='Hide Access Menu')
