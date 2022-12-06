from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTests(TestCase):

    def test_create_user(self):
        """
        # 0. User.objects.count() == 0
        # 1. client.get url create_user  :  username, first_name, last_name, password1, password2
        # 2. User.objects.first()  =>  user  => username, first_name
        """
        self.assertEqual(User.objects.count(), 0)
        test_data = {
            'username': 'das',
            'first_name': 'das1',
            'last_name': 'das2',
            'password1': '123',
            'password2': '123',
        }
        response = self.client.post(reverse('user_create'), test_data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.first()
        self.assertEqual(user.username, test_data['username'])
        self.assertEqual(user.first_name, test_data['first_name'])
        self.assertEqual(user.last_name, test_data['last_name'])

