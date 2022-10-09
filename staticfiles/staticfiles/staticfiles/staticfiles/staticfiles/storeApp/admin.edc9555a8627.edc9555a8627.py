from django.contrib import admin
from .models import Product,Customer, Category, Order, OrderItem

admin.site.site_header = "Samuel_Online Shoppers_Database Admin"
admin.site.index_title = "Online Shoppers Administration"
admin.site.site_title = "Online Shoppers Administration"

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)