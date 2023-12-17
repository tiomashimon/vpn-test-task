from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponse
from ..website.models import UserWebsite
from django.views import View
from ..website.forms import UserWebsiteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..website.services import get_base_url
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from .tasks import send_email_task



from PIL import Image
from .models import Profile
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO  


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
            email = request.POST.get('email')

            # subject = 'Thank you for registering!'
            # message = f"Thank you for registering on our platform. We're excited to have you as a member of our community!\n\nBest regards,\nThe Team"
            print('Message sent to', email)
            # send_email_task.delay(subject, message, [email])



            user = form.save(commit=False)
            user.email = email
            user.save()
            login(request, user)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Please enter valid data :)'})



class StatsListView(View, LoginRequiredMixin):
    template_name = 'user/stats.html'
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        error = ''

        if not request.user.is_authenticated:
            return redirect('login')
        
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
            url = get_base_url(form.cleaned_data['url'])
            existing_website = UserWebsite.objects.filter(user=request.user, url=url).first()

            if existing_website:
                error = 'Website with this URL already exists.'
            else:
                user_website = form.save(commit=False)
                user_website.user = request.user
                user_website.url = get_base_url(form.instance.url)
                user_website.save()  

        context = {
            'user': request.user,
            'websites': websites,
            'form': form,
            'error': error
        }
        return render(request, self.template_name, context)





class ProfileView(View, LoginRequiredMixin):
    template_name = 'user/profile.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            websites = UserWebsite.objects.filter(user=request.user)
            total_websites, total_received_data, total_sent_data, total_clicks = 0, 0, 0, 0
            for website in websites:
                total_websites += 1
                total_received_data += website.data_received
                total_sent_data += website.data_sent
                total_clicks += website.clicks

            context = {
                'total_websites': total_websites,
                'total_received_data': total_received_data,
                'total_sent_data': total_sent_data,
                'total_clicks': total_clicks
            }
            return render(request, self.template_name, context)
        else:
            return redirect('login')


    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        profile_image = request.FILES.get('profile_image')

        user = request.user
        user.email = email
        user.first_name = firstname
        user.last_name = lastname

        if profile_image:

            image = Image.open(profile_image)
            image = image.convert('RGB')

            output = BytesIO()
            image.save(output, format='JPEG')
            output.seek(0)

            profile_image = SimpleUploadedFile(profile_image.name, output.read(), content_type='image/jpeg')

            profile, created = Profile.objects.get_or_create(user=user)
            profile.avatar.save(profile_image.name, ImageFile(profile_image), save=True)

        user.save()

        return redirect('profile')
