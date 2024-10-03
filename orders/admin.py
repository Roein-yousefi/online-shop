from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order , OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order','product' , 'quantity' , 'price']

class OrderAdmin(ModelAdminJalaliMixin , admin.ModelAdmin):
    list_display = ('user' , 'is_paid', 'first_name' , 'last_name' , 'datetime_added')

    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order' , 'product','quantity' , 'price')

admin.site.register(OrderItem, OrderItemAdmin)
