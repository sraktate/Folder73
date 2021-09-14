from .models import Product
from django.contrib import admin

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Provider','Product_name','Price','Quantity','Amount','Stock']


admin.site.register(Product,ProductAdmin)