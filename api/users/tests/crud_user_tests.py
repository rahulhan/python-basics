from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from users.models import GlobalConfig
from rest_framework.authtoken.models import Token


class UserAddTest(TestCase):
    """
        Usage: python manage.py test users.tests
    """
    def setUp(self):
        """
            Create test objects
        """
        self.c = Client()
        self.user_obj = User.objects.create_user(
            "testuser",
            "testuser@test.com", "testuser"
        )
        self.token = Token.objects.create(key="testuser", user=self.user_obj)

        self.global_config = GlobalConfig.objects.create(
            name="token_exp",
            value="60"
        )

    def tearDown(self):
        """
            Destroy test objects
        """
        User.objects.all().delete()

    def test_empty_username(self):
        """
            Test of empty username as input
        """
        print("hi")
        data = '{"username": "", "password": "test"}'
        response = self.c.post(
            "/users/add/",
            data, content_type="application/json",
            **{"HTTP_AUTHORIZATION": "Token testuser"})
        self.assertEqual(response.status_code, 400)

    def test_user_already_exists(self):
        """
            Test to duplicate user
        """
        data = '{"username": "testuser", "password": "test"}'
        response = self.c.post(
            '/users/add/',
            data, content_type="application/json",
            **{"HTTP_AUTHORIZATION": "Token testuser"})
        self.assertEqual(response.status_code, 400)
 
    def test_add_user(self):
        """
            Test to adding user
        """
        data = '{"username": "testuser1", "password": "test"}'
        response = self.c.post(
            '/users/add/',
            data, content_type="application/json",
            **{"HTTP_AUTHORIZATION": "Token testuser"})
        self.assertEqual(response.status_code, 200)
