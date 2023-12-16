from django.urls import path
from .views import UserWebsiteCreateView, proxy_view

urlpatterns = [
    path('create/', UserWebsiteCreateView.as_view(), name='website-create'),
    path('<str:user_site_name>/<path:routes_on_original_site>/', proxy_view, name='proxy'),
]

