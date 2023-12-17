import time
from .models import UserWebsite
import re
from .services import get_base_url




class TrafficMeasurementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    
    def bytes_to_megabytes(self, bytes_size):
        megabytes = bytes_size / (1024 ** 2)
        return megabytes


    def __call__(self, request):
        response = self.get_response(request)

        if '/website/' in request.path:
            path_segments = request.path.split('/')

            if len(path_segments) >= 4:
                user_site_name = path_segments[2]
                routes_on_original_site = '/'.join(path_segments[3:])
                
                name = user_site_name
                user = request.user if request.user.is_authenticated else None

                if user:
                    user_website = UserWebsite.objects.filter(name=name).first()
                    
                    if user_website:
                        data_sent = self.bytes_to_megabytes(len(request.body) if request.body else 0)
                        data_received = self.bytes_to_megabytes(len(response.content))

                        user_website.data_sent += data_sent
                        user_website.data_received += data_received
                        user_website.save()

        return response

