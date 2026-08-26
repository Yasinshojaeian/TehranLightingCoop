from django.contrib import admin

from Article.models import Article, Category
from parler.admin import TranslatableAdmin


# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = (
        'title',
        'status',
        'created',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'translations__title',
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }


@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = (
        'title',
        'category',
        'status',
        'author',
        'created',
    )

    list_filter = (
        'status',
        'category',
    )

    search_fields = (
        'translations__title',
        'translations__description',
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }
