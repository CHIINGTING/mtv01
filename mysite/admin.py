from django.contrib import admin
from .models import newTable

# Register your models here.

class tableAdmin(admin.ModelAdmin):


admin.site.register(newTable)

