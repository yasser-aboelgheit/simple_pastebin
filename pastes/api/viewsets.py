from pastes.models import Paste
from .serializers import PasteSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters


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