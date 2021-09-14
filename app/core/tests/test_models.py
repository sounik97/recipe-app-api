from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        ''' Test creating with a new suer email is succesfull'''

        email = 'test@londonappdev.com'
        password = 'TestPass123'

        user = get_user_model().objects.create_user(
               email = email,
               password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''
        Test the new user email domain is normalized and lowercased'''

        email = 'test@LONDONAPPDEV.com'

        user = get_user_model().objects.create_user(
               email,
               'test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test for creating user with no email error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        ''' test for creating superuser'''
        user = get_user_model().objects.create_superuser(
        'test@londonappdev.com', 'Test123'
        )

        ''' is_superuser is included in the  PermissionsMixin in models.py '''

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
