from rest_framework import serializers
from pastes.models import Paste
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','password')



class PasteSerializer(serializers.HyperlinkedModelSerializer):
    privacy_choiches = (('public','public'),
                        ('only_me','only_me'),
                        ('custome','custome'),)
    url = serializers.HyperlinkedIdentityField(view_name="paste-detail")
    author = serializers.ReadOnlyField()
    privacy = serializers.ChoiceField(choices=privacy_choiches)
    class Meta:
        model = Paste
        fields = ('id', 'url','author','privacy','allow', 'name', 'code', 'created')
