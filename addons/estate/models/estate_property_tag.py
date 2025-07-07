from odoo import models, fields, api # type: ignore

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    
    name = fields.Char(required=True)