from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.utils.text import slugify

from extenstions.utils import jalali_converter_date
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

from django.db import models
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    STATUS_CATEGORY = (
        ('1', 'پیش نویس'),
        ('2', 'منتشرشده'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CATEGORY,
        default='1'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    translations = TranslatedFields(
        title=models.CharField(
            max_length=255,
            verbose_name='عنوان'
        ),

        slug=models.SlugField(
            max_length=300,
            allow_unicode=True,
            verbose_name='اسلاگ'
        ),
    )

    def __str__(self):
        return self.safe_translation_getter(
            'title',
            any_language=True
        ) or ''

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def jalali_converter_date(self):
        return jalali_converter_date(self.created)


class Article(TranslatableModel):
    STATUS_ARTICLE = (
        ('1', 'پیش نویس'),
        ('2', 'منتشرشده'),
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
        verbose_name='دسته بندی'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(
        max_length=1,
        choices=sorted(STATUS_ARTICLE),
        verbose_name='وضعیت'
    )

    image = models.ImageField(
        upload_to='article/images',
        null=True,
        verbose_name='کاور مقاله'
    )

    read_time = models.IntegerField(
        verbose_name='زمان مطالعه',
        null=True
    )

    created = models.DateTimeField(
        null=True,
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )

    updated = models.DateTimeField(
        null=True,
        auto_now=True,
        verbose_name='تاریخ آپدیت'
    )

    translations = TranslatedFields(
        title=models.CharField(
            max_length=255,
            verbose_name='عنوان'
        ),
        slug=models.SlugField(
            max_length=300,
            allow_unicode=True,
            blank=True,
            verbose_name='اسلاگ'
        ),

        description=RichTextField(
            verbose_name='توضیحات'
        ),

        seo_title=models.CharField(
            max_length=255,
            null=True,
            blank=True,
            verbose_name='عنوان سئو'
        ),

        meta_description=models.CharField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name='توضیحات متا'
        ),

        meta_keywords=models.CharField(
            max_length=500,
            null=True,
            blank=True,
            verbose_name='کلمات کلیدی متا'
        ),
    )

    def save(self, *args, **kwargs):
        if self.safe_translation_getter('slug', any_language=True) is None:
            title = self.safe_translation_getter(
                'title',
                any_language=True
            )

            if title:
                self.slug = slugify(title, allow_unicode=True)

        super().save(*args, **kwargs)
