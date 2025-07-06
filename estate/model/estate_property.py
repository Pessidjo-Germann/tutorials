from odoo import fields,models

class EstateProperty(models.Model):
    _name="estate.property"
    _description= 'This is module to test my work'
    
    name=fields.Char(required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean('garden',default=True)
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
        string='garden orientation',
        selection=[('North','South'),('East','West')]
    )