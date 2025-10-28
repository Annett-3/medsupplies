# medsupplies/urls.py

from django.contrib import admin
from django.urls import path
from shop import views  # make sure your views.py is in the shop app

urlpatterns = [
    path('admin/', admin.site.urls),

    # Website pages
    path('', views.home, name='home'),                # Homepage
    path('services/', views.services, name='services'),
    path('staff/', views.staff, name='staff'),
    path('equipments/', views.equipments, name='equipments'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

