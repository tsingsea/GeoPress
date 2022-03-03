from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    return HttpResponse('register')























# https://www.django-rest-framework.org/tutorial/quickstart/#views
from django.contrib.auth.models import Group
from auth2.models import User
from rest_framework import viewsets
from rest_framework import permissions
from auth2.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]