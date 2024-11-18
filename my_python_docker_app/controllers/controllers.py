# controllers/controllers.py
from odoo import http

class MyDockerController(http.Controller):
    @http.route('/my_docker_app/hello', auth='public', website=True)
    def hello_world(self):
        return "<h1>Hello, world from My Python Docker App!</h1>"