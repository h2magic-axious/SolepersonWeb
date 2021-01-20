from django.utils.deprecation import MiddlewareMixin


class CorsMiddleWare(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response["Access-Control-Allow-Origin"] = "*"
        return response
