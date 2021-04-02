from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

class util(models.Model):
    _name = 'util'

    def resta(self, var1):
        print(var1)