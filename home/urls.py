from django.urls import path,include
from .views import *
app_name = "home"
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('price', price, name='price'),
    path('portfolio', portfolio, name='portfolio'),
    path('elements', elements, name='elements'),
    path('contact', contact, name='contact'),
]