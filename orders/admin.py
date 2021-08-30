from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone']
