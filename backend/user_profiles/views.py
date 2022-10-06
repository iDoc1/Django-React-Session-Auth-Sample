from re import L
from django.contrib.auth.models import User  # Django-provided User model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from .serializers import UserProfileSerializer


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user  # Get user that sent the request
            username = user.username

            user = User.objects.get(id=user.id)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error': 'Error occurred while getting user profile'})


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = request.user
            username = user.username

            data = request.data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            city = data['city']

            UserProfile.objects.filter(user=user).update(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                city=city
            )

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error': 'Error occurred while updating user profile'})
