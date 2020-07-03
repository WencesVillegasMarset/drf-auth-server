from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from users.models import User


class AuthenticationTests(APITestCase):
    # TODO 1: Testear login fallido
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'juan@juan.com', password='juan123')
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        user = {
            'username': 'juan@juan.com',
            'password': 'juan123'
        }
        response = self.client.post('/api/users/login', data=user)
        # print(response.data)
        self.assertEqual(self.token.key, response.data['token'])

    def test_register_while_logged_in_and_valid_data(self):
        new_user = {
            'email': "pedro@pedro.com",
            'password': "pedrito123",
            'password2': "pedrito123"
        }
        response = self.client.post(
            '/api/users/register',
            data=new_user, format='json',
            HTTP_AUTHORIZATION="Token "+self.token.key)
        self.assertEqual(response.status_code, 201)

    def test_register_while_logged_in_and_non_matching_passwords(self):
        new_user = {
            'email': "pedro@pedro.com",
            'password': "pedrito123",
            'password2': "a"
        }
        response = self.client.post(
            '/api/users/register',
            data=new_user, format='json',
            HTTP_AUTHORIZATION="Token "+self.token.key)
        self.assertEqual(response.status_code, 400)

    def test_logout_successful(self):
        response = self.client.get(
            '/api/users/logout', HTTP_AUTHORIZATION="Token " + self.token.key)

        self.assertEqual(response.status_code, 200)

    def test_logout_unauthorized(self):
        response = self.client.get(
            '/api/users/logout', HTTP_AUTHORIZATION="a")
        self.assertEqual(response.status_code, 401)
