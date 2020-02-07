#-*- coding:utf-8 -*-

# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from odoo import api, fields, models
from odoo import exceptions, _


class LcReport(models.AbstractModel):
    _name = 'report.sales_tax_invoice.report_lc' #report.modulename.your_modelname of report


   @api.multi
    def render_html(self, docids, data=None):
        comp_sales = self.env["res.company"].search([])

        acct_invoice = self.env["account.invoice"].search([("id","=",docids)])
        if  acct_invoice.partner_id.supplier == False:
            pid = acct_invoice.partner_id.id
            cust_invoice = self.env["res.partner"].search([('id','=',pid)])
            table_data = self.env["account.invoice"].search([("id","=",docids)]).invoice_line_ids
            for r in table_data:
                s=0
                for t in r.invoice_line_tax_ids:
                    s= s+t.amount
                    
                    
            date_inv=""
            if acct_invoice.date_invoice:
                date_inv=(datetime.strptime(acct_invoice.date_invoice, "%Y-%m-%d")).strftime("%d-%m-%Y")    
            docargs = {
                'datas':comp_sales,
                'account':acct_invoice,
                'customer':cust_invoice,
                'table_data':table_data,
                'date':date_inv
            }
            
            return self.env['report'].render('sales_tax_invoice.report_lc',docargs)
        else:
            raise exceptions.ValidationError(_("This Report is only for Sales Order"))
     
     
