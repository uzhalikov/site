from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserContacts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 'photo']

class UserContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts()
        fields = ['id', 'name', 'link']