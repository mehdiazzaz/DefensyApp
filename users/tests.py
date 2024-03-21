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
        self.assertTrue(form.is_valid())

    def test_user_register_form_invalid_data(self):
        form = UserRegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)  # There are 4 required fields

    def test_user_update_form_valid_data(self):
        form = UserUpdateForm(data={
            'username': 'newusername',
            'email': 'newemail@example.com',
        })
        self.assertTrue(form.is_valid())

    def test_user_update_form_invalid_data(self):
        form = UserUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)  # There are 2 required fields

    def test_profile_update_form_valid_data(self):
        form = ProfileUpdateForm(data={
            'image': 'test_image.png'
        })
        self.assertTrue(form.is_valid())

    def test_profile_update_form_invalid_data(self):
        form = ProfileUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)  # There is 1 required field
