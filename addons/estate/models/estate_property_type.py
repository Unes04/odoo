from odoo import models, fields, api # type: ignore

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    
    name = fields.Char(required=True)