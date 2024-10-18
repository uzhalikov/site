from django.shortcuts import render
from .models import *
from .serializers import PreviewPostSerializer, PostSerializer, PreviewPoemSerializer, PoemSerializer
from .decorators import post_viewing, get_unread_post
import re

@get_unread_post
def about(request, **kwargs):
    context = {
        'unread': kwargs['unread'],
        'title': 'Об авторе',
        'post': PostSerializer(Post.objects.get(is_published=False)).data
    }
    return render(request, 'blog/about.html', context)

@get_unread_post
def posts(request, **kwargs):
    context = {
        'unread': kwargs['unread'],
        'title': 'Статьи',
        'description': 'Читать авторские статьи на тему программирования с полного нуля, на таких языках программирования как Python и Javascript, без лишней воды и непонятного слэнга.',
        'posts': PreviewPostSerializer(Post.objects.filter(is_published=True), many=True, context={"request": request}).data
    }
    return render(request, 'blog/posts.html', context)

@get_unread_post
def poems(request, **kwargs):
    context = {
        'unread': kwargs['unread'],
        'title': 'Стихи',
        'description': 'Читать авторские стихотворения Халикова Ульфата Жэудатовича, начинающего поэта из Санкт-Петербурга. Только личные произведения, без каких либо современных помощников.',
        'poems': PreviewPoemSerializer(Poem.objects.all(), many=True).data
    }
    return render(request, 'blog/poems.html', context)

@get_unread_post
@post_viewing
def show_post(request, slug, **kwargs):
    context = {
        'unread': kwargs['unread'],
        'prev_url': 'posts',
        'title': 'Статьи',
        'item': PostSerializer(kwargs['item']).data
    }
    return render(request, 'blog/post.html', context)

@get_unread_post
def show_poem(request, poem_id, **kwargs):
    item = PoemSerializer(Poem.objects.get(id=poem_id)).data
    description = re.sub("^\s+|\n|\r|\s+$", '', item['poem'])
    context = {
        'unread': kwargs['unread'],
        'prev_url': 'poems',
        'title': 'Стихи',
        'item': item,
        'description': description[:160]
    }
    return render(request, 'blog/poem.html', context)

@get_unread_post
def questions(request, **kwargs):
    questions = Question.objects.filter(answer__isnull=False)
    context = {
        'unread': kwargs['unread'],
        'title': 'Вопросы',
        'description': 'Задать любой интересующий вопрос владельцу сайта анонимно, просмотреть список заданных вопросов. Не нашли нужной информации на сайте? Задайте вопрос и получите развернутый ответ',
        'questions': questions,
    }
    return render(request, 'blog/questions.html', context)