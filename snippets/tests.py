from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm

# Create your tests here.
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from snippets.models import Snippet, User
from rest_framework import serializers



class Setup(TestCase):
    def setUp(self):
        User.objects.create_user(username='test--user')
        User.objects.create_user(username='second--user')
        Snippet.objects.create(title='Snippet Title', code='print hello world', owner_id='1')
        Snippet.objects.create(title='Second Snippet Title', code='print world hellow', owner_id='2')

class BasicMathTestCase(TestCase):
    def test_math(self):
        a = 1
        b = 1
        self.assertEqual(a+b, 2)

    def test_failing_case(self):
        a = 1
        b = 0
        self.assertEqual(a+b, 1)


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        create a new account object
        """
        url = reverse('user-list')
        data = {'username': 'TestAccount'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data, data)

    def test_create_account_username_error(self):
        """
        error when using space in username
        """
        url = reverse('user-list')
        data = {'username': 'Test Account'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_clean_username_exception(self):
        # Create a user to test it is already taken
        User.objects.create_user(username='test--user')

        url = reverse('user-list')
        data = {'username': 'test--user'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # setup form for testing
        form = UserCreationForm()
        form.cleaned_data = data

        # use a context manager to watch for validation error
        with self.assertRaises(serializers.DjangoValidationError):
            form.clean_username()


class APIResponseTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test--user')
        self.snippet = Snippet.objects.create(title='Snippet Title', code='print hello world', owner_id='1' )

    def test_users_response(self):
        response = self.client.get('/users/1/')
        data = {'username': 'test--user'}

        def extractDictAFromB(A, B):
            return dict([(k, B[k]) for k in A.keys() if k in B.keys()])
        self.assertEqual(data, extractDictAFromB(data, response.data))
        # self.assertDictContainsSubset({'username': 'test--user'}, response.data)


class ModelTestCase(TestCase):
    def setUp(self):
        self.snippet = Snippet.objects.create(title='Snippet Title', code='print hello world', owner_id='1' )

    def test_create_snippet(self):
        """
        Test that a snippet is created
        """
        self.assertEqual(self.snippet.title, 'Snippet Title')
        self.assertEqual(self.snippet.code, 'print hello world')
        self.assertEqual(self.snippet.owner_id, '1')

    def test_create_snippet_highlight_created(self):
        """
        test the snippet highlight is created
        html line 82
        """
        html_line_82 = '<h2>{}</h2>'.format(self.snippet.title)
        self.assertIn(html_line_82, self.snippet.highlighted)

    def test_snippet_detail(self):
        testsnippet = Snippet.objects.all()[0]
        url = '/snippets/{}/'.format(str(testsnippet.id))
        response = self.client.get(url)
        self.assertContains(response, testsnippet.title)