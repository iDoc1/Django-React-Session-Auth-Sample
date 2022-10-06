from django.contrib import auth
from django.contrib.auth.models import User  # Django-provided User model
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from user_profiles.models import UserProfile


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        
        try:
            user = request.user
            is_authenticated = user.is_authenticated  # Attribute that tells if user is logged in

            if is_authenticated:
                return Response({'is_authenticated': 'success'})
            else:
                return Response({'is_authenticated': 'error '})
        except:
            return Response({'error': 'Error occurred when checking authentication'})


@method_decorator(csrf_protect, name='dispatch')  # Ensure signup is CSRF protected
class SignupView(APIView):
    """
    Handles requests to create a new user
    """
    permission_classes = (permissions.AllowAny, )  # Allow anyone to get signup view

    def post(self, request, format=None):
        data = request.data

        try: 
            username = data['username']
            password = data['password']
            re_password = data['re_password']

                   
            # Check if passwords match
            if password == re_password:            

                # Ensure username does not already exist
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'})
                elif len(password) < 6:
                    return Response({'error': 'Password must be at leat 6 characters long'})
                else:

                    # Create user
                    user = User.objects.create_user(username=username, password=password)

                    # Create empty user profile associated with this account
                    user = User.objects.get(id=user.id)
                    UserProfile.objects.create(
                        user=user,
                        first_name='',
                        last_name='',
                        phone='',
                        city=''
                    )

                    return Response({'success': 'User account successfully created'})            
            else:
                return Response({'error': 'Passwords do not match'})
        except:
            return Response({'error': 'Error occurred while registering account'})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )  # Allow anyone to get login view

    def post(self, request, format=None):
        data = request.data

        username = data['username']
        password = data['password']

        try:
            # Check if given user/password is valid
            user = auth.authenticate(username=username, password=password)  # Gets User object
            if user is not None:
                auth.login(request, user)  # Saves userID in the sesson
                return Response({'success': 'User is authenticated', 'username': username})
            else:
                return Response({'error': 'Error authenticating'})
        except:
            return Response({'error': 'Error occurred while logging in'})


class LogoutView(APIView):   
    def post(self, request, format=None):
        try:
            auth.logout(request)  # Clears session data for user sending the request
            return Response({'success': 'Logged out'})
        except:
            return Response({'error': 'Error occurred when loggin out'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    """
    Sets a CSRF cookie when this view is requested
    """
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        return Response({ 'success': 'CSRF cookie set' })


class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = request.user  # Get currently logged in user
        
        try:
            user = User.objects.filter(id=user.id).delete()
            return Response({'success': 'User successfully deleted'})
        except:
            return Response({'error': 'Error occurred while trying to delete user'})


class GetUsersView(APIView):
    """
    Returns JSON list of all users. Not really necessary if admin superuser exists.
    """
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)  # Return JSON serialized response
