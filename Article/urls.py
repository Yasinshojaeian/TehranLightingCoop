from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article_list'),
    path('detail/<str:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/list/<str:slug>/', CategoryArticleListView.as_view(), name='category_list'),

]
