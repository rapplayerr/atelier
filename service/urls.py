from django.urls import path
from . import views
urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('<slug:category_slug>/<slug:service_slug>/', views.service_detail, name='service_detail'), 
    # path('create', views.create, name='create'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    # path('<int:pk>/update', views.Update.as_view(), name='update'),
    # path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
