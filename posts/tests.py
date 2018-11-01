#importing sample database
from django.test import TestCase
from django.urls import reverse

#importing Post to test
from .models import Post

#using TestCase because need to know the HomePageView
#works with the database
# Create your tests here.

class PostModelTest(TestCase):
#created a class with a method to create a new database
#that has one entry post with a text field
#and text saying, just a test
    def setUp(self):
        Post.objects.create(text='just a test')
#this function runs the test
    def test_text_content(self):
        post = Post.objects.get(id=1)
        #lets us put variables directly in strings
        #as long as surrounded by {}
        #setting expected_object_name to be the
        #string of the value post.text
        expected_object_name = f'{post.text}'
        #assertEqual checks that our created entry matches
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):
#200 means throwing an HTTP 200 response
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
