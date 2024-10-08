from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

class Poem(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    poem = models.TextField(verbose_name='Стихотворение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title if self.title else 'Poem without title'

    class Meta:
        verbose_name_plural = 'Стихотворения'

class Question(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор вопроса')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Вопросы'

class PostCategory(models.Model):
    category = models.CharField(max_length=255, verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    def __str__(self):
        return self.category
        
    class Meta:
        verbose_name_plural = 'Категории постов'

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True, null=True)
    post = models.TextField(verbose_name='Содержимое')
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name='Категория')
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(verbose_name='Опубликован', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Посты'
        ordering = ['-id']

    def get_views_count(self):
        return self.views_count.count()


class PostViews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='views_count')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    class Meta:
        verbose_name_plural = 'Просмотры постов'

    def __str__(self):
        return self.post.title