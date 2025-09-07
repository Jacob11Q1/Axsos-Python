from django.contrib import admin
from .models import Product, Order

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','created_at')
    list_display_links = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity','price_at_purchase','total_price','created_at')
    ordering = ('-created_at',)