from django.urls import path
from .views import UserAPIView, UserContactsAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('contacts/', UserContactsAPIView.as_view())
]