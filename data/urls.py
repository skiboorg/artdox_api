from django.urls import path,include
from . import views

urlpatterns = [
    path('banners', views.GetBanners.as_view()),
    path('c_form', views.CForm.as_view()),






]
