from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home , name = "home"),
    path('login',views.loginPage , name = 'signin'),
    path('signup',views.registerPage , name = 'signup'),
    path('logout',views.logoutPage , name = "logout"),
    path('admin-site',views.admin_site , name="admin-site"),
    path('hospital-admin',views.admin_home , name="hospital-admin"),
    path('signup-admin',views.adminRegister , name="admin-Register"),
    path('inside/<str:pk>',views.next , name="inside"),
]