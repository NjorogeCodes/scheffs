from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('services/',views.services,name='services'),
    path('team/',views.team,name='team'),
    path('testimonials/',views.testimonial,name='testimonial'),
    path('booking/',views.booking,name='booking'),

]