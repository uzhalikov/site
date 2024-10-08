from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Poem, Post, Question, PostViews
from .serializers import PoemSerializer, QuestionSerializer, PostSerializer, PreviewPostSerializer, PreviewPoemSerializer
from .utils import get_ip
import requests

class CheckCaptcha(ListAPIView):
    def post(self, request):
        url = f"https://www.google.com/recaptcha/api/siteverify?secret={request.POST['key']}&response={request.POST['response']}"
        response = requests.request("GET", url)
        return Response(response.json().get("success", False))
        
class PoemAPIView(ListAPIView):
    serializer_class = PoemSerializer

    def get_queryset(self):
        return Poem.objects.filter(id=self.kwargs['id'])

class PostAPIView(ListAPIView):
    lookup_field = 'slug'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'])

    def put(self, request, slug):
        obj = super().get_object()
        ip = get_ip(request)
        PostViews.objects.get_or_create(post=obj, ip_address=ip)
        return Response(PostSerializer([obj], many=True, context={"request": request}).data)

class PreviewPoemListAPIView(ListAPIView):
    queryset = Poem.objects.all()
    serializer_class = PreviewPoemSerializer

class PreviewPostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    
    def get(self, request):
        params = self.request.query_params.get('filter', '')
        data = PreviewPostSerializer(self.queryset.filter(is_published=True, post__iregex=params), many=True, context={"request": request})
        return Response(data.data)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(answer__isnull=False)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'text': 'Спасибо за вопрос, он появится в общем списке, как только владелец на него ответит'})

class UnreadPostAPIView(ListAPIView):
    def get(self, request):
        ip = get_ip(request)
        return Response({'count': Post.objects.filter(is_published=True).count() - PostViews.objects.filter(ip_address=ip).count()})