from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Article, Category


# Create your views here.

class ArticleListView(View):
    template_name = 'Article/blog.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(status='2')
        articles = Article.objects.filter(status='2')

        return render(request, self.template_name,
                      context={'articles': articles, 'articles_categories': categories})


class CategoryArticleListView(View):
    template_name = 'Article/blog.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(status='2')
        category = get_object_or_404(Category, slug=kwargs['slug'])
        articles = Article.objects.filter(status='2', category=category)

        return render(request, self.template_name,
                      context={'articles': articles, 'articles_categories': categories})


class ArticleDetailView(View):
    template_name = 'Article/blog-details.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(status='2')

        article = get_object_or_404(
            Article.objects.language(request.LANGUAGE_CODE),
            translations__slug=kwargs['slug'],
            translations__language_code=request.LANGUAGE_CODE,
        )

        other_articles = (
            Article.objects
            .language(request.LANGUAGE_CODE)
            .filter(status='2')
            .exclude(id=article.id)
        )

        return render(
            request,
            self.template_name,
            context={
                'article': article,
                'other_articles': other_articles,
                'categories': categories,
            }
        )
