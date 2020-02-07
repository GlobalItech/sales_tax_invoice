#This code contains addition of some fields
from odoo import fields, models, api
from docutils.nodes import field
class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    sal_tax_inv = fields.Char('Sale Tax Invoice')
    


class ProductTemplate(models.Model):
    _inherit = "product.template"
     
    color = fields.Char('Color')
     
 
class Company(models.Model):
    _inherit = "res.company"
     
    sales_tax_no = fields.Char('Sales Tax No.')
    nat_tax_no = fields.Char('National Tax No.')
     
class Partner(models.Model):
    _inherit = "res.partner"
     
    sales_tax_no = fields.Char('Sales Tax No.')
    nat_tax_no = fields.Char('National Tax No.')