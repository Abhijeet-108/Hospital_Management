from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('login',views.loginPage , name="signin"),
    path('signup',views.registerPage , name="signup"),
    path('logout',views.logoutPage , name="logout"),
    path('admin1', views.admin1, name='admin'),
    path('booking', views.booking, name='booking'),
    path('hospital/<str:hospital_name>/', views.hospital_detail, name='hospital_detail'),
]
