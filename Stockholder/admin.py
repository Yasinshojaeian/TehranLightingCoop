from django.contrib import admin
from parler.admin import TranslatableAdmin

from Stockholder.models import Stockholder


@admin.register(Stockholder)
class StockholderAdmin(TranslatableAdmin):
    list_display = [
        'full_name',
        'display_position',
        'position',
        'order',
    ]

    list_filter = [
        'position',
    ]

    search_fields = [
        'translations__first_name',
        'translations__last_name',
    ]

    fieldsets = (
        ('اطلاعات شخصی', {
            'fields': (
                'first_name',
                'last_name',
                'position',
                'position_custom',
                'order',
            )
        }),
    )
