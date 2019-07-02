from pastes.models import Paste
from .serializers import PasteSerializer
from rest_framework import viewsets

class PasteViewSet(viewsets.ModelViewSet):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer