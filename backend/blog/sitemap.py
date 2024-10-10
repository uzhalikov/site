from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *


class AboutViewSitemap(Sitemap):
    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['posts']

    def location(self, item):
        return reverse(item)

class PoemSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['poems']

    def location(self, item):
        return reverse(item)

class QuestionSitemap(Sitemap):
    changefreq = 'daily'
    
    def items(self):
        return ['questions']

    def location(self, item):
        return reverse(item)

class PostViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return f'/post/{item.slug}/'

class PoemViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Poem.objects.all()

    def location(self, item):
        return f'/poem/{item.id}/'


sitemaps = {
    'about': AboutViewSitemap,
    'post': PostViewSitemap,
    'posts': PostSitemap,
    'poem': PoemViewSitemap,
    'poems': PoemSitemap,
    'questions': QuestionSitemap
}