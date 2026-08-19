from django.contrib import admin

from Article.models import Article, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}