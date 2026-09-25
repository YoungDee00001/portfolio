from django.urls import path
from .views import about, contact, resume, services, view_my_work

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path ('resume/', resume, name='resume'),
    path ('contact/', contact, name='contact'),
    path ('view_my_work/', view_my_work, name='view_my_work'),
    
    
]
