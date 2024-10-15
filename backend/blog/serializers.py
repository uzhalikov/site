from rest_framework import serializers
from .models import Post, PostViews, Poem, Question
from .utils import get_ip
import re
from django.utils.safestring import mark_safe

class PoemSerializer(serializers.ModelSerializer):
    prev_p = serializers.SerializerMethodField()
    next_p = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    theme = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = ['id', 'created', 'author', 'poem', 'prev_p', 'next_p', 'title', 'theme']

    def get_prev_p(self, obj):
        try:
            return obj.get_previous_by_created().id
        except Exception:
            pass
                
    def get_theme(self, obj):
        return obj.theme.theme

    def get_created(self, obj):
        return obj.created.strftime('%d.%m.%Y')

    def get_next_p(self, obj):
        try:
            return obj.get_next_by_created().id
        except Exception:
            pass

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

class PreviewPoemSerializer(serializers.ModelSerializer):
    poem = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = ['id', 'created', 'author', 'poem']
    
    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_poem(self, obj):
        return "".join(obj.poem.splitlines(keepends=True)[:2])

class PreviewPostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    read = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'post', 'created', 'author', 'image', 'read', 'slug']

    def get_post(self, obj):
        return f'{re.sub(r"<[^>]+>", "", obj.post[:180])}...'

    def get_created(self, obj):
        return obj.created.strftime('%d.%m.%Y')

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_read(self, obj):
        ip_address = get_ip(self.context.get('request'))
        return bool(PostViews.objects.filter(post=obj, ip_address=ip_address))

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    prev_p = serializers.SerializerMethodField()
    next_p = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = ['id', 'title', 'post', 'image', 'created', 'author', 'views', 'prev_p', 'next_p', 'tags', 'slug']

    def get_created(self, obj):
        return obj.created.strftime('%d.%m.%Y')

    def get_tags(self, obj):
        return list(obj.tags.all().values('id', 'name'))

    def get_post(self, obj):
        return mark_safe(obj.post)

    def get_prev_p(self, obj):
        try:
            prev_obj = obj.get_previous_by_created()
            if prev_obj.is_published:
                return prev_obj.slug
            return prev_obj.get_previous_by_created().slug
        except Exception:
            pass

    def get_next_p(self, obj):
        try:
            next_obj = obj.get_next_by_created()
            if next_obj.is_published:
                return next_obj.slug
            return next_obj.get_next_by_created().slug
        except Exception:
            pass

    def get_views(self, obj):
        return obj.get_views_count()

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        depth = 1