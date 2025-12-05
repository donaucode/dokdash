from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name="contact_list"),
    path('create/', views.contact_create, name="contact_create"),
    path('<uuid:contact_pk>/', views.contact_read, name="contact_read"),
    path('<uuid:contact_pk>/update/', views.contact_update, name="contact_update"),
    
    path('<uuid:contact_pk>/informations/create/', views.contact_information_create, name="contact_information_create"),
    
]