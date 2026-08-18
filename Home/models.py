from django.db import models

from extenstions.utils import jalali_converter_date


# Create your models here.


class Slider(models.Model):
    SLIDER_STATUS = (
        ('1', 'غیرفعال'),
        ('2', 'فعال'),
    )
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name='عنوان')
    image = models.ImageField(upload_to='home/sliders', null=True, blank=True, verbose_name='تصویر')
    status = models.CharField(max_length=1, default='1', choices=SLIDER_STATUS, verbose_name='وضعیت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'


class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    text = models.TextField(verbose_name='نظر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def created_jalali(self):
        return jalali_converter_date(self.created)

    class Meta:
        verbose_name = 'ارتباط ما با'
        verbose_name_plural = 'ارتباط با ما'
