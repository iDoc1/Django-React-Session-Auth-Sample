import imp
from django.urls import path
from .views import SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, GetUsersView

urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view(), name='authenticated'),
    path('register', SignupView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('delete', DeleteAccountView.as_view()),
    path('csrf_cookie', GetCSRFToken.as_view()),
    path('users', GetUsersView.as_view())
]
