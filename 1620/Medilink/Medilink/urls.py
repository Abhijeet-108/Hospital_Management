from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('beds.urls'))
    path('')
    // My name is abhijeet
    
]
