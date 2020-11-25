# from django.test import TestCase
import os, django
import random

from django.urls import reverse

from JWT_Auth.utils import generate_jwt, obtain_payload
from unit_tests.JWT_Auth import user_data

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_server.settings')
django.setup()
from rest_framework.test import APIClient
from unittest import TestCase


class JWTTest(TestCase):
    """测试接口是否正常"""

    @classmethod
    def setUpClass(cls):
        cls.user = random.choice(user_data)

    def test_jwt_function(self):
        jwt_token = generate_jwt(self.user)
        self.assertEqual(type(jwt_token), str, msg=f"jwt_token not is str {jwt_token}")
        payload = obtain_payload(jwt_token)
        self.assertEqual(self.user, payload, msg=f"obtain_payload fail {payload}")

    def test_jwt_view(self):
        client = APIClient(enforce_csrf_checks=True)
        res_get = client.post(reverse("jwt_auth:get_jwt"), self.user, format="json")
        jwt_token = res_get.data["data"]
        self.assertEqual(type(jwt_token), str, msg=f"res_get not jwt_token {jwt_token}")
        res_verify = client.post(reverse("jwt_auth:verify_jwt"), {"jwt": jwt_token}, format="json")
        user = res_verify.data["data"]
        self.assertTrue(user["user"] == self.user["user"], msg=f"verify fail user {user}")

    @classmethod
    def tearDownClass(cls):
        pass
