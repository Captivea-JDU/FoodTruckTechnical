# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):

    _inherit = "sale.order"
    self['x_studio_email'] = self.partner_id.email

    


