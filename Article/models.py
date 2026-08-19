from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.utils.text import slugify

from extenstions.utils import jalali_converter_date


# Create your models here.

class Category(models.Model):
    STATUS_CATEGORY = (
        ('1', 'پیش نویس'),
        ('2', 'منتشرشده'),
    )

    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', allow_unicode=True)
    status = models.CharField(max_length=1, choices=STATUS_CATEGORY, default='1')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def jalali_converter_date(self):
        return jalali_converter_date(self.created)


class Article(models.Model):
    STATUS_ARTICLE = (
        ('1', 'پیش نویس'),
        ('2', 'منتشرشده'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles',
                                 verbose_name='دسته بندی')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', allow_unicode=True, null=True, blank=True, max_length=300)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = RichTextField()
    status = models.CharField(max_length=1, choices=sorted(STATUS_ARTICLE), verbose_name='وضعیت')
    image = models.ImageField(upload_to='article/images', null=True, verbose_name='کاور مقاله')
    read_time = models.IntegerField(verbose_name='زمان مطالعه', null=True)
    created = models.DateTimeField(null=True, auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(null=True, auto_now=True, verbose_name='تاریخ آپدیت')
    seo_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='عنوان سئو')
    meta_description = models.CharField(max_length=500, null=True, blank=True, verbose_name='توضیحات متا')
    meta_keywords = models.CharField(max_length=500, null=True, blank=True, verbose_name='کلمات کلیدی متا')

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def jalali_converter_date(self):
        return jalali_converter_date(self.created)

    def updated_jalali(self):
        return jalali_converter_date(self.updated)

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)
