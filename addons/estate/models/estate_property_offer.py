from odoo import models, fields, api # type: ignore
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'
    
    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    
    _inherit = 'estate.property.offer'
    
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date:
                offer.date_deadline = offer.create_date + relativedelta(days=offer.validity)
            else:
                offer.date_deadline = fields.Date.today() + relativedelta(days=offer.validity)
    
    def _inverse_date_deadline(self):
        for offer in self:
            if offer.create_date and offer.date_deadline:
                offer.validity = (offer.date_deadline - offer.create_date.date()).days
            elif offer.date_deadline:
                offer.validity = (offer.date_deadline - fields.Date.today()).days