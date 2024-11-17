from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('services/', views.services, name='services'),
    path('menu/',views.menu,name='menu'),
    path('booking/',views.booking,name='booking'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),






]