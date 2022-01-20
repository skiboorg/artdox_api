from django.urls import path,include
from . import views

urlpatterns = [
    path('banners', views.GetBanners.as_view()),
    path('c_form', views.CForm.as_view()),
    path('r_form', views.RForm.as_view()),
    path('s_form', views.SForm.as_view()),






]
