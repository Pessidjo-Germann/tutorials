from odoo import fields,models
from dateutil.relativedelta import relativedelta
from datetime import date
class EstateProperty(models.Model):
    _name="estate.property"
    _description= 'This is module to test my work'
    
    name=fields.Char(required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False,default=lambda self: date.today() + relativedelta(months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean('garden',default=True)
    garden_area=fields.Integer(),
    active=fields.Boolean(),
    garden_orientation=fields.Selection(
        string='garden orientation',
        selection=[('North','South'),('East','West')]
    ),
    property_type_id=fields.Many2one("estate.property.type",string="property")
    state = fields.Selection(
    selection=[
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ],
    required=True,
    copy=False,
    default='new'
)