from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_Text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_name=f'{post.text}'
        self.assertEqual(excepted_object_name,'just a test')

    