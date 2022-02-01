from django.contrib import admin
from .models import *


class OrderItemFileInline (admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemFileInline]

admin.site.register(Order,OrderAdmin)
