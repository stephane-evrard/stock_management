from django.contrib import admin

# Register your models here.
from .models import *
from .forms import  *


# admin.site.register(Stock)

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)