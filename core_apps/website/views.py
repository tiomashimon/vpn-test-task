from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from .models import UserWebsite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import requests
from django.http import HttpResponse

class UserWebsiteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'website/website_create.html'
    login_url = 'login'
    model = UserWebsite
    fields = ['name', 'url']

    def get_success_url(self):
        return reverse('login')
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)



def proxy_view(request, user_site_name, routes_on_original_site):
    user = request.user
    website_exists = UserWebsite.objects.filter(user=user, url=routes_on_original_site).first()

    if website_exists:
        website_exists.clicks += 1
        website_exists.save()
        
        try:
            response = requests.get(routes_on_original_site)
            response_text = response.text
        except requests.RequestException as e:
            response_text = 'Requested Website dont answering'
    else:
        response_text = 'Enter Valid Data'

    return HttpResponse(response_text)


    