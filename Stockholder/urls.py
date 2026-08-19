from django.urls import path
from .views import StockholderListView, StockholderDetailView

app_name = 'stockholder'

urlpatterns = [
    path('list/', StockholderListView.as_view(), name='list'),
    path('detail/<int:pk>/', StockholderDetailView.as_view(), name='detail'),
]