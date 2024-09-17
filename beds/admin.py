from django.contrib import admin
from .models import hosp , inventory , blood

# Register your models here.

admin.site.register(hosp)
admin.site.register(inventory)
admin.site.register(blood)