
{
    'name' : 'Sales Tax Invoice',
    'category': 'Invoices',
    'summary':'Pakistan Sales Tax Invoice',
    'description' : "This module will be give sale tax invoices print. ",
    'author' : 'Itech resources',
    'website' : 'www.itechresources.com',
    
    'depends' : [
                    'account','product'
                ],
    'data' :[
                'views/account_invoice_views_custom.xml',
                'reports/lc_report_menu.xml',
                'reports/report.xml',
            ],
    'installable' : True,
    'price':20.00,
    'currency':'EUR', 
}
