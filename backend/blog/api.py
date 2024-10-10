from django.http import JsonResponse
from .models import Question
from .serializers import QuestionSerializer
import requests
from backend.settings import reCAPTCHA_SECRET_KEY

def get_all_questions(request):
    return JsonResponse(list(Question.objects.filter(answer__isnull=False).values()), safe=False)

def create_question(request):
    url = f"https://www.google.com/recaptcha/api/siteverify?secret={reCAPTCHA_SECRET_KEY}&response={request.POST['g-recaptcha-response']}"
    response = requests.request("GET", url)
    result = response.json().get("success", False)
    if result:
        serializer = QuestionSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse('success', safe=False)
    return JsonResponse('error', safe=False)