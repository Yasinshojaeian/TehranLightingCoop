from django.db import models
from django.utils.text import slugify


class Stockholder(models.Model):
    """مدل سهامداران شرکت"""

    # انتخاب‌های سمت
    POSITION_CHOICES = [
        ('ceo', 'مدیرعامل'),
        ('chairman', 'رئیس هیئت مدیره'),
        ('vice_chairman', 'نایب رئیس هیئت مدیره'),
        ('board_member', 'عضو هیئت مدیره'),
        ('manager', 'مدیر'),
        ('supervisor', 'ناظر'),
        ('shareholder', 'سهامدار'),
        ('other', 'سایر'),
    ]

    # فیلدهای اصلی
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="سمت")
    position_custom = models.CharField(max_length=100, blank=True, null=True, verbose_name="سمت (سفارشی)")

    # فیلدهای زمانی
    joined_date = models.DateField(auto_now_add=True, verbose_name="تاریخ加入")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    order = models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name = "سهامدار"
        verbose_name_plural = "سهامداران"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def display_position(self):
        """نمایش سمت - اگر سفارشی بود از آن استفاده کن"""
        if self.position == 'other' and self.position_custom:
            return self.position_custom
        return self.get_position_display()
