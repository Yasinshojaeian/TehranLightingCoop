from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام شما *'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تلفن *'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control py-3',
                'placeholder': 'نظر شما *',
                'rows': '4'
            }),
        }
