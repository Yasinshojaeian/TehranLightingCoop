from django.contrib import admin
from .models import Stockholder


@admin.register(Stockholder)
class StockholderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'display_position']
    list_filter = ['position']
    search_fields = ['first_name', 'last_name']

    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'position', 'position_custom','order')
        }),

    )
