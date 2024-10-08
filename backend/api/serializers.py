from rest_framework import serializers
from .models import Post, Poem, Question, PostViews
from .utils import get_ip

class PoemSerializer(serializers.ModelSerializer):
    prev_p = serializers.SerializerMethodField()
    next_p = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author')

    class Meta:
        model = Poem
        fields = ['id', 'created', 'author_name', 'poem', 'prev_p', 'next_p', 'title']

    def get_prev_p(self, obj):
        try:
            return obj.get_previous_by_created().id
        except Exception:
            pass

    def get_next_p(self, obj):
        try:
            return obj.get_next_by_created().id
        except Exception:
            pass

class PreviewPoemSerializer(serializers.ModelSerializer):
    poem = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = ['id', 'created', 'author', 'poem']
    
    def get_author(self, obj):
        return str(obj.author)

    def get_poem(self, obj):
        return "".join(obj.poem.splitlines(keepends=True)[:2])

class PreviewPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.SerializerMethodField()
    read = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'post', 'created', 'author', 'image', 'read', 'slug']

    def get_post(self, obj):
        return f'{obj.post[:180]}...'

    def get_read(self, obj):
        ip_address = get_ip(self.context.get('request'))
        return bool(PostViews.objects.filter(post=obj, ip_address=ip_address))

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    views = serializers.SerializerMethodField()
    prev_p = serializers.SerializerMethodField()
    next_p = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        fields = ['id', 'title', 'post', 'image', 'created', 'author', 'views', 'prev_p', 'next_p', 'tags', 'slug']

    def get_tags(self, obj):
        return list(obj.tags.all().values('id', 'name'))

    def get_prev_p(self, obj):
        try:
            return obj.get_previous_by_created().slug
        except Exception:
            pass

    def get_next_p(self, obj):
        try:
            return obj.get_next_by_created().slug
        except Exception:
            pass

    def get_views(self, obj):
        return obj.get_views_count()

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        depth = 1