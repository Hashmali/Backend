import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import User
from .serializers import UserSerializer,RegistrationSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={"phone":"0502184560","first_name":"dgdsg",
        "second_name":"dfgd","image":"null","password":"ahmad","password2":"ahmad","is_admin":"true"}
        response=self.client.post("register/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.token=Token.objects.create(user=self.user)
        self.test_auth()

    def test_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)