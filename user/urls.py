from django.urls import path,include
from . import views

urlpatterns = [


    path('me/', views.GetUser.as_view()),
    path('update', views.UserUpdate.as_view()),
    path('recover_password', views.UserRecoverPassword.as_view()),
    path('withdrawal_request', views.WithdrawalRequestView.as_view()),
    path('payment_types', views.PaymentSystems.as_view()),



]
