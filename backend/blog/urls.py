from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('', about, name='about'),
    path('questions', questions, name='questions'),
    path('posts', posts, name='posts'),
    path('poems', poems, name='poems'),
    path('post/<slug:slug>', show_post, name='post'),
    path('poem/<int:poem_id>', show_poem, name='poem'),
    path('api/create_question', create_question),
    path('api/questions', get_all_questions),
]