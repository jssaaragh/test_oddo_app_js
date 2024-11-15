from odoo import http

class MyController(http.Controller):
    @http.route('/my_module/hello', auth='public', website=True)
    def hello(self):
        return "<h1>Welcome to My Docker-Based Odoo App!</h1>"