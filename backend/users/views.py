from rest_framework.generics import ListAPIView
from .serializers import UserSerializer, UserContactsSerializer
from .models import UserContacts, User

class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserContactsAPIView(ListAPIView):
    queryset = UserContacts.objects.all()
    serializer_class = UserContactsSerializer