from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'expiry_date', 'is_expired')
    list_filter = ('expiry_date',)
