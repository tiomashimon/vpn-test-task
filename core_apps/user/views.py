from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from ..website.models import UserWebsite
from django.views import View
from ..website.forms import UserWebsiteForm

class SignUpView(CreateView):
    model = User
    template_name = 'user/signup.html'
    form_class =UserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form':form, 'error':'Please enter valid data :)'})


class StatsListView(View):
    template_name = 'user/stats.html'

    def get(self, request, *args, **kwargs):
        error = ''
        form = UserWebsiteForm()
        websites = UserWebsite.objects.filter(user=request.user)


        context = {
            'user': request.user,
            'websites': websites,
            'form': form,
            'error': error
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        error = ''
        form = UserWebsiteForm(request.POST)
        websites = UserWebsite.objects.filter(user=request.user)

        if form.is_valid():
            user_website = form.save(commit=False) 
            user_website.user = request.user  
            user_website.save()  

        context = {
            'user': request.user,
            'websites': websites,
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)
