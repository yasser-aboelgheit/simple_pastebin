from rest_framework import serializers
from pastes.models import Paste
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','password')




# class TestSerializer(serializers.ModelSerializer):
#     allowed = serializers.ChoiceField(choices=userList)
#
#     class Meta:
#         model = Test
#         fields = ('allowed',)


class PasteSerializer(serializers.HyperlinkedModelSerializer):
    # allow = serializers.SerializerMethodField()
    privacy_choiches = (('public','public'),
                        ('only_me','only_me'),
                        ('custome','custome'),)
    url = serializers.HyperlinkedIdentityField(view_name="paste-detail")
    # if Paste.author:
    author = serializers.ReadOnlyField()
    privacy = serializers.ChoiceField(choices=privacy_choiches)
    print ("HERE")
    print(str(Paste.name))
    # if privacy == 'custome':
    #     print ("HELLO")
    class Meta:
        model = Paste
        fields = ('id', 'url','author','privacy','allow', 'name', 'code', 'created')

    # def get_name(self, obj):
    #     print ("inside content")
    #     print (obj.privacy)
    #     # print (self.privacy)
    #     return obj.name

    # def get_allow(self, obj):
    #     print ("inside allow")
    #     return obj.allow
    # def __init__(self, *args, **kwargs):
    #     # initialize fields
    #     super(PasteSerializer, self).__init__(*args, **kwargs)
    #     # now modify the creditcard field
    #     self.fields['allow'] = serializers.ReadOnlyField()