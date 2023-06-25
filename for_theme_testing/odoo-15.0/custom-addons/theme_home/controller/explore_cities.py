from odoo import http
from odoo.http import request


class ExploreCities(http.Controller):

    @http.route('/cities', type='json', auth='public', website=True, csrf=False)
    def all_cities(self,**kwargs):
        cities = http.request.env['yh.cities'].search_read([], ['country_id', 'state_id', 'image'])
        return cities


class Slider(http.Controller):

    @http.route('/slide', auth="public", type="json")
    def all_slide(self):
        slides = http.request.env['carousel.view'].search([])
        slide_data = []
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for slide in slides:
            slide_data.append({
                'id': slide.id,
                'name': slide.title,
                'image_url': f"{base_url}/web/image/carousel.view/{slide.id}/image",
            })
        print(slide_data)
        return slide_data