from odoo import http
from odoo.http import request


class ExploreCities(http.Controller):

    @http.route('/cities', type='json', auth='public', website=True, csrf=False)
    def all_cities(self,**kwargs):
        cities = http.request.env['yh.cities'].search_read([], ['country_id', 'state_id', 'image'])
        return cities
