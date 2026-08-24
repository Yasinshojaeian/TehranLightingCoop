from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stockholder


class StockholderListView(ListView):
    """نمایش لیست سهامداران"""
    model = Stockholder
    template_name = 'Stockholder/stockholder_list.html'
    context_object_name = 'stockholders'
    ordering = ['last_name']

    def get_queryset(self):
        return Stockholder.objects.all().order_by('order')
