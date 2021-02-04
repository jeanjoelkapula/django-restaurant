from django.contrib import admin
from .models import MenuItem,  MenuItemOption, MenuItemAddOn, Order, OrderItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(MenuItemOption)
admin.site.register(MenuItemAddOn)
admin.site.register(Order)
admin.site.register(OrderItem)
