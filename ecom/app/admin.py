from django.contrib import admin
from .models import Product
# Register your models here.

# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_id', 'prod_name', 'pro_desc','pro_img', 'pro_cat']
    
admin.site.register(Product,ProductAdmin)