from django.urls import path,include
from .views import *
app_name = "home"
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
]