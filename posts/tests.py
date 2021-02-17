from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class DbPageTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view(self):
        resp = self.client.get('/db')
        self.assertEqual(resp.status_code, 200)

    def test_view_by_name(self):
        resp = self.client.get(reverse('db'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('db'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'db.html')