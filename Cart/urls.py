from django.urls import path,include
from . import views

urlpatterns = [
    path('add', views.AddToCart.as_view()),
    path('get', views.GetCart.as_view()),





]
