from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .models import NewUser 
from django.http import Http404

# Create your views here.

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve a User instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        try:
            return NewUser.objects.get(id=id)
        except NewUser.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        task = self.get_object(id)
        serializer = UserSerializer(task)
        return Response(serializer.data)
