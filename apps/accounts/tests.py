from django.test import TestCase
from .models import User
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Model

class TestUserModel(TestCase):
    def setUp(self):
        self.model = User

    def test_create_user_with_valid_data_succeeds(self):
        self.model.objects.create_user(email='user@mail.com', password='#pass1234')
        qs = self.model.objects.filter(email='user@mail.com')
        self.assertTrue(qs.exists())

    def test_create_user_without_password_fails(self):
        with self.assertRaises(ValueError) : 
            self.model.objects.create_user(email='user@mail.com', password='')

    def test_create_user_without_email_fails(self):
        with self.assertRaises(ValueError) : 
            self.model.objects.create_user(email='', password='#pho3nix9q')

    def test_create_staffuser(self):
        self.model.objects.create_staffuser(email='user@mail.com', password='#pass1234')
        qs = self.model.objects.get(email='user@mail.com')
        self.assertFalse(qs.admin)

    def test_create_superuser(self):
        self.model.objects.create_superuser(email='user@mail.com', password='#pass1234')
        qs = self.model.objects.get(email='user@mail.com')
        self.assertTrue(qs.admin)

            
