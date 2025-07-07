from odoo import models, fields, api
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
    
    # Add these fields
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        store=True  # Add this if you want to store the value in DB
    )
    
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date:
                offer.date_deadline = fields.Date.to_date(offer.create_date) + relativedelta(days=offer.validity)
            else:
                offer.date_deadline = fields.Date.today() + relativedelta(days=offer.validity)
    
    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                if offer.create_date:
                    offer.validity = (offer.date_deadline - fields.Date.to_date(offer.create_date)).days
                else:
                    offer.validity = (offer.date_deadline - fields.Date.today()).days