from odoo import fields,models


class EstateOffer(models.Model):
    _name="estate.property.offer"
    _description= "offer to estate"
    
    price=fields.Float(string="prix")
    status=fields.Selection(
        string="Status",
        selection=[("accepted","Accepted"),("refused","Refused")]
    )
    partner_id =fields.Many2one('res.partner', string='Partenaire',required=True)
    property_id=fields.Many2one('estate.property',string='proprietaire',required=True)
    
    