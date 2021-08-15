from django.contrib import admin
from .models import newTable, Product
from django.db.models import *


# Register your models here.
class adminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'qty')


admin.site.register(newTable)
admin.site.register(Product, adminProduct)
