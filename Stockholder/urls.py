from django.urls import path
from .views import StockholderListView

app_name = 'stockholder'

urlpatterns = [
    path('list/', StockholderListView.as_view(), name='list'),
]