from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.grocery_create,name='create_grocery')
]