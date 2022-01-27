from django.urls import path,include
from . import views

urlpatterns = [
    path('create', views.CreateOrder.as_view()),
    path('get', views.GetOrders.as_view()),
    path('get_order_item', views.GetOrderItem.as_view()),
    path('payment_notify', views.PaymentNotify.as_view()),
    path('test', views.Test.as_view()),


]
