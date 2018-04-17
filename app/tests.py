from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from app.models import Signup


class SignupTestCase(TestCase):
    def setUp(self):
        Signup.objects.create(email="wasuaje@gmail.com")
        Signup.objects.create(email="wasuaje@hotmail.com")

    def test_signup_are_correct(self):
        """Animals that can speak are correctly identified"""
        gm = Signup.objects.get(email="wasuaje@gmail.com")
        hm = Signup.objects.get(email="wasuaje@hotmail.com")
        self.assertEqual(gm.email, 'wasuaje@gmail.com')
        self.assertEqual(hm.email, 'wasuaje@hotmail.com')
