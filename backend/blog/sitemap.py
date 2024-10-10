from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *

class AboutViewSitemap(Sitemap):
    def items(self):
        return ['about']

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

class PoemPreviewViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Poem.objects.all()

    def location(self, item):
        return f'/poems'

class PostPreviewViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return f'/posts'

class QuestionViewSitemap(Sitemap):
    changefreq = 'daily'
    
    def items(self):
        return Question.objects.all()

    def location(self, item):
        return f'/question'