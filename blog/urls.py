from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus, name='about'),
    path('footer/', views.footer, name='footer'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]
