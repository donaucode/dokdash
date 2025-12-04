from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name="trip_list"),
    path('<uuid:trip_pk>/', views.trip_read, name="trip_read"),
]
