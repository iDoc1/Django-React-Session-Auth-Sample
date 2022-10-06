from urllib import response
from .test_setup import TestUserSetup


class UserSignUpTestCase(TestUserSetup):
    def test_register_user_fails_with_no_data(self):
        """
        Attempting to register a user with no data responds with an error
        """
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)

    def test_register_user_succeeds(self):
        """
        Attempting to register a user with correct data succeeds
        """
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.data)

    def test_register_user_fails_if_password_too_short(self):
        """
        Attempting to register a user with a password less than 6 chars responds with 
        error
        """
        bad_user_data = {
            "username": "fakeuser",
            "password": "pass",
            "re_password": "pass"
        }
        response = self.client.post(self.register_url, bad_user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)

    def test_register_user_fails_if_passwords_do_not_match(self):
        """
        Attempting to register a user with a password less than 6 chars responds with 
        error
        """
        bad_user_data = {
            "username": "fakeuser",
            "password": "password",
            "re_password": "password45"
        }
        response = self.client.post(self.register_url, bad_user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)

    def test_cannot_register_user_if_username_already_exists(self):
        """
        Attempting to register a username that alredy exists responds with an error
        """
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)


class UserLoginTestCase(TestUserSetup):
    def test_user_cannot_login_with_wrong_username(self):
        """
        Logging in with correct password but wrong username responds with an error
        """
        wrong_user_data = {
            "username": "fakeuser45",
            "password": "password",
        }
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, wrong_user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)

    def test_user_cannot_login_with_wrong_password(self):
        """
        Logging in with correct username but wrong password responds with an error
        """
        wrong_user_data = {
            "username": "fakeuser",
            "password": "password45",
        }
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, wrong_user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.data)

    def test_user_can_log_in_successfully(self):
        """
        Logging in with correct password but wrong username responds with an error
        """
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.data)

    def test_user_can_log_out_successfully(self):
        """
        Logging a user out that is already logged in is successful
        """
        self.client.post(self.register_url, self.user_data, format="json")
        self.client.post(self.login_url, self.user_data, format="json")
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.data)

    def test_user_not_logged_in_is_not_authorized(self):
        """
        If a user is not logged in then the check authentication view returns an error
        """
        response = self.client.get(self.authenticated_url)
        self.assertEqual(response.status_code, 403)
        self.assertIn("detail", response.data)  # Django 403 response details expected

    def test_user_logged_in_is_authorized(self):
        """
        If a user is logged in then the check authentication view returns a a success
        """
        self.client.post(self.register_url, self.user_data, format="json")
        self.client.post(self.login_url, self.user_data, format="json")
        response = self.client.get(self.authenticated_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("success", response.data["is_authenticated"])

