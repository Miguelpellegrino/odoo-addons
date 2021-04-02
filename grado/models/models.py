# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class vacunas(models.Model):
    _name = 'vacuna'

    name = fields.Char()
    lote = fields.Char()
    cantidad = fields.Integer()
    description = fields.Text()

    @api.constrains('lote')
    def lote_check(self):
        search_lote = self.search_count([('lote', '=', self.lote)])
        if search_lote > 1: raise Warning("Ya existe en el lote: %s" % self.lote)

    def resta(self):
        util = self.env['util'].resta(self.lote)