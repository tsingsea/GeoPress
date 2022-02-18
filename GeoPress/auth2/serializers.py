# https://www.django-rest-framework.org/tutorial/quickstart/#serializers
from django.contrib.auth.models import Group
from auth2.models import User
from rest_framework import serializers

# 把 Python 对象转换为 JSON ，这被称为序列化（serialization）
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']