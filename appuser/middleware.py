from ipware import get_client_ip
from .models import IpData



class IPIsValid:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        IpData(ip=ip).save()


        response = self.get_response(request)
        return response