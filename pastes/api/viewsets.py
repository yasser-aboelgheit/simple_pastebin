from pastes.models import Paste
from .serializers import PasteSerializer,UserSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PasteFilter(filters.FilterSet):
    class Meta:
        model = Paste
        fields = {
            'created':['iexact', 'lte', 'gte', ],
        }



class PasteViewSet(viewsets.ModelViewSet):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer
    filterset_class = PasteFilter
    permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=str(self.request.user))
        else:
            serializer.save()


