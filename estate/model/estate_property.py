from odoo import fields,models,api
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
    garden_area=fields.Integer()
    active=fields.Boolean()
    garden_orientation=fields.Selection(
        string='garden orientation',
        selection=[('North','South'),('East','West')]
    ),
    property_type_id=fields.Many2one("estate.property.type",string="property")
    tag_ids=fields.Many2many("estate.property.tag",string="Tag")
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    seller_id=fields.Many2one('res.partner',string='Buyer')
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
    offer_ids=fields.One2many("estate.property.offer","property_id",string='Offer')
    total_area=fields.Float(compute="_area_total")
    best_price=fields.Float(compute="_get_price")
    
    @api.depends("garden_area")
    def _area_total(self):
        for record in self:
            record.total_area=record.garden_area+record.living_area
            
    @api.depends("offer_ids")
    def _get_price(self):
        for record in self:
            record.best_price=max(record.offer_ids.mapped("price"))        
            