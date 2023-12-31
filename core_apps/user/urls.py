from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, StatsListView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html', success_url = 'stats'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('stats/', StatsListView.as_view(), name='stats'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
