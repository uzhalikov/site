# Generated by Django 4.2.15 on 2024-10-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('poem', models.TextField(verbose_name='Стихотворение')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name_plural': 'Стихотворения',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('post', models.TextField(verbose_name='Содержимое')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
            ],
            options={
                'verbose_name_plural': 'Категории постов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='Автор вопроса')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views_count', to='api.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name_plural': 'Просмотры постов',
            },
        ),
    ]
