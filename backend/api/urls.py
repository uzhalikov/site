from django.urls import path
from .views import PoemAPIView, PreviewPostListAPIView, QuestionListAPIView, PostAPIView, UnreadPostAPIView, PreviewPoemListAPIView, CheckCaptcha

urlpatterns = [
    path('poems/', PreviewPoemListAPIView.as_view()),
    path('poem/<int:id>', PoemAPIView.as_view()),
    path('posts/unread/', UnreadPostAPIView.as_view()),
    path('posts/', PreviewPostListAPIView.as_view()),
    path('post/<slug:slug>', PostAPIView.as_view()),
    path('questions/', QuestionListAPIView.as_view()),
    path('check_captcha/', CheckCaptcha.as_view()),
]