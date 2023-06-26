from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.contact_us, name='contact-us'),
    path('register/', views.register, name='register'),
    path('donation/', views.donation, name='donation'),
]
