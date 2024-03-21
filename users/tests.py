from django.test import TestCase
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

class TestForms(TestCase):
    def test_user_register_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        

    def test_user_register_form_invalid_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())

    def test_user_update_form_valid_data(self):
        form = UserUpdateForm(data={
            'username': 'newusername',
            'email': 'newemail@example.com',
        })
        self.assertTrue(form.is_valid())

    def test_user_update_form_invalid_data(self):
        form = UserUpdateForm(data={})
        self.assertFalse(form.is_valid())

    def test_profile_update_form_valid_data(self):
        form = ProfileUpdateForm(data={})
        self.assertTrue(form.is_valid())

    def test_profile_update_form_invalid_data(self):
        form = ProfileUpdateForm(data={})
        self.assertTrue(form.is_valid())
