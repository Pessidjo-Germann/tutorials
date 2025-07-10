from odoo import fields,models

class TypeProperty(models.Model):
    _name="estate.property.type"
    _description="Type of real state"
    
    name=fields.Char(required=True)