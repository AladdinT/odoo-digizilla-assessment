from odoo import models, fields

class Tag(models.Model):
    _name = "model.tag"

    name = fields.Char()
    # digizilla_ids = fields.Many2many('digizilla', string='Member')