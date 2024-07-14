from django.urls import path
from . import views

urlpatterns=[
    path('api/contacts/',views.get_details, name='get_details'),
    path('api/contacts/',views.view_booking,name='view_booking')
]