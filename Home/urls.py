from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contatc/', ContactUsView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
]
