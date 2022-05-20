# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):

	recipe = fields.Char(string='Recipe')

    _inherit = "sale.order"

    record['x_studio_email'] = record.partner_id.email

    return record


