from odoo import models, fields


class YourHome(models.Model):
    _name = "yh.cities"
    _description = "Your Home Cities"

    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string="State")
    description = fields.Text()
    image = fields.Binary()


class SlideShow(models.Model):
    _name = 'carousel.view'
    _description = 'Carousel View'

    title = fields.Char(string='Title')
    sub_title = fields.Char(string='Sub Title')
    image = fields.Binary(string='Image')
