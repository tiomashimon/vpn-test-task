from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from .models import UserWebsite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import requests
from django.http import HttpResponse
from urllib.parse import urlparse
from .services import get_base_url, change_html_href


# class UserWebsiteCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'website/website_create.html'
#     login_url = 'login'
#     success_url = 'stats'
#     model = UserWebsite
#     fields = ['name', 'url']

#     def get_success_url(self):
#         return reverse('login')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.url = get_base_url(form.instance.url)

#         return super().form_valid(form)



def proxy_view(request, user_site_name, routes_on_original_site):
    user = request.user
    base_url = get_base_url(routes_on_original_site)
    website_exists = UserWebsite.objects.filter(name=user_site_name).first()
    if website_exists:
        website_exists.clicks += 1
        website_exists.save()

        try:
            response = requests.get(base_url)
            response_text = change_html_href(response, user_site_name, base_url)
        except requests.RequestException as e:
            response_text = 'Requested Website dont answering'
    else:
        response_text = 'Enter Valid Data'

    return HttpResponse(response_text)


