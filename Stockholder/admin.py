from django.contrib import admin
from .models import Stockholder


@admin.register(Stockholder)
class StockholderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'display_position', 'share_percentage', 'phone', 'email', 'order', 'is_active']
    list_filter = ['position', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['order', 'is_active', 'share_percentage']
    ordering = ['order', 'last_name']

    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'position', 'position_custom', 'image')
        }),
        ('اطلاعات تماس', {
            'fields': ('phone', 'email')
        }),
        ('اطلاعات سهام', {
            'fields': ('share_percentage', 'share_count')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('bio', 'order', 'is_active')
        }),
    )