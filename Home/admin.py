from django.contrib import admin

from Home.models import Slider, ContactUs, Album, Gallery
from parler.admin import TranslatableAdmin

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GalleryAdmin(admin.TabularInline):
    model = Gallery


@admin.register(Album)
class AlbumAdmin(TranslatableAdmin):
    list_display = ('title',)
    inlines = [GalleryAdmin]
