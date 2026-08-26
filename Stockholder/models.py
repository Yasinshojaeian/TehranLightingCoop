from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Stockholder(TranslatableModel):
    """مدل سهامداران شرکت"""

    POSITION_CHOICES = [
        ('ceo', _('مدیرعامل')),
        ('chairman', _('رئیس هیئت مدیره')),
        ('vice_chairman', _('نایب رئیس هیئت مدیره')),
        ('board_member', _('عضو هیئت مدیره')),
        ('manager', _('مدیر')),
        ('supervisor', _('ناظر')),
        ('shareholder', _('سهامدار')),
        ('other', _('سایر')),
    ]

    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        verbose_name=_("سمت")
    )

    joined_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("تاریخ عضویت")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("آخرین بروزرسانی")
    )

    order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_("ترتیب")
    )

    translations = TranslatedFields(
        first_name=models.CharField(
            max_length=100,
            verbose_name=_("نام")
        ),

        last_name=models.CharField(
            max_length=100,
            verbose_name=_("نام خانوادگی")
        ),

        position_custom=models.CharField(
            max_length=100,
            blank=True,
            null=True,
            verbose_name=_("سمت سفارشی")
        ),
    )

    class Meta:
        verbose_name = _("سهامدار")
        verbose_name_plural = _("سهامداران")

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def display_position(self):
        if self.position == 'other' and self.position_custom:
            return self.position_custom

        return self.get_position_display()