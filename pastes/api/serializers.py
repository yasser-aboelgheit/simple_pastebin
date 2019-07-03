from rest_framework import serializers
from pastes.models import Paste
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class PasteSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="paste-detail")

    if Paste.author:
        author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Paste
        fields = ('id', 'url', 'author', 'name', 'code', 'created')
