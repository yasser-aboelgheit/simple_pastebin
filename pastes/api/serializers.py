from rest_framework import serializers
from pastes.models import Paste

class PasteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Paste
        fields = ('name', 'code', 'created')
