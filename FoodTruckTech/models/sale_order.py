# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
	
    _inherit = "sale.order"

    record['x_studio_email'] = record.partner_id.email

    return record

