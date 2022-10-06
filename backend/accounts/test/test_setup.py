"""
This file was adapted from the following source:
https://www.youtube.com/watch?v=17KdirMbmHY&ab_channel=CryceTruly
"""

from django.urls import reverse
from rest_framework.test import APITestCase


class TestUserSetup(APITestCase):
    """
    Creates a fake user to run the tests with
    """

    def setUp(self) -> None:
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.authenticated_url = reverse("authenticated")

        self.user_data = {
            "username": "fakeuser",
            "password": "password",
            "re_password": "password"
        }

    def tearDown(self) -> None:
        return super().tearDown()
