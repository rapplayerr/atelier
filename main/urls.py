from django.urls import path
from . import views
urlpatterns = [
    path('', views.glavnaya, name='home'),
    path('about/', views.about, name='about')
]