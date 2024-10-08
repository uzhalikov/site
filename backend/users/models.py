from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(verbose_name='Фото', upload_to='images/', null=True, blank=True)
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class UserContacts(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контакты пользователей'