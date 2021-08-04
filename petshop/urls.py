from django.urls import path
from .views import *

urlpatterns = [
    path('pet/', pet, name='pet'),
    path('pet/<str:petId>/', edit_pet, name='edit_pet'),
    path('pet/delete/<str:petId>/', delete_pet, name='delete_pet'),
]