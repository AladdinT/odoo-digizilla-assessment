from odoo import models, fields

class Digizilla(models.Model):
    _name = "model.digizilla"
    _description = "Digizilla Member"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name    = fields.Char(string='Name', required=True, tracking=1)
    gender  = fields.Selection( 
        [ 
            ('male', 'Male'),
            ('female', 'Female')
        ], string='Gender' , tracking=1)
    country     = fields.Char(string='Country', default="Egypt" , tracking=1)
    joining_date = fields.Date(string='Joining Date' , tracking=1)
    tag_ids     = fields.Many2many('model.tag', string='Tags' , tracking=1)
    customer_ids = fields.Many2many('res.partner', string='Customers' , tracking=1)
    company_id  = fields.Many2one('res.company', string='Company', required=True , tracking=1)
    notes       = fields.Text(string='Notes' , tracking=1)
    comments    = fields.Char(string='Comments' , tracking=1)
