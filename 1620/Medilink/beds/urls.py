from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('login',views.loginPage , name="signin"),
    path('signup',views.registerPage , name="signup"),
    path('logout',views.logoutPage , name="logout")
]
