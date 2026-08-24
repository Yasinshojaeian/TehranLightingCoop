from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from Article.models import Article
from Home.models import Slider, Album, Gallery
from Stockholder.models import Stockholder
from .forms import ContactUsForm


# Create your views here.

class HomeView(View):
    template_name = 'Home/index.html'

    def get(self, request, *args, **kwargs):
        stockholders = Stockholder.objects.all().order_by('order')
        albums = Album.objects.all()
        sliders = Slider.objects.filter(status='2')
        articles = Article.objects.filter(status='2')
        last_article = articles.last()
        mor = []
        for item in articles:
            if item.id != last_article.id:
                mor.append(item)

        return render(request, self.template_name,
                      context={'sliders': sliders, 'articles': mor, 'last_article': last_article,
                               'stockholders': stockholders, 'albums': albums})


class AboutUsView(View):
    template_name = 'Home/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class ContactUsView(View):
    template_name = 'Home/contact.html'
    form_class = ContactUsForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      context={'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد', 'success')
            return redirect('home:contact')
        else:
            for f in form:
                for error in f.errors:
                    messages.error(request, error, 'danger')
        return redirect('home:contact')


class AlbumsView(View):
    template_name = 'Home/album.html'

    def get(self, request, *args, **kwargs):
        albums = Album.objects.all()
        return render(request, self.template_name, context={'albums': albums})


class AlbumDetailView(View):
    template_name = 'Home/album-details.html'

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album, pk=kwargs['pk'])
        images = Gallery.objects.filter(album=album)
        return render(request, self.template_name, context={'images': images, 'album': album})
