from django.test import TestCase
from post_engine.models import Post, Comment
from django.contrib.auth.models import User
from django.test.client import Client
from model_bakery import baker

# class TestPostModels(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user('john','john@j.jcom','johnpassword')
#
#         def TestCreatePost(self):
#             user1 =  self.client.login(username='john', password='johnpassword')
#             posts = Post.objects.create(user='user1',post='hi am home')
#             likes = posts.likes.set(user1)
#             # self.assertEqual(likes.count(), 1)
#             self.assertEqual(get_total_likes(), likes.count())
#             self.assertEqual(str(user),'tom')


class TestPostModels(TestCase):
    def test_post_model(self):
        post_user = User.objects.create_user('john','johnpassword')
        post = Post.objects.create(post= "hi there", user=post_user)
        user = Post.objects.create(user=post_user)
        self.assertEqual(str(user), 'john')

    def test_comment_model(self):

        comment_user = User.objects.create_user('ana','anapassword')
        post_user = User.objects.create_user('john','johnpassword')
        post = Post.objects.create(post= "hi there", user=post_user)
        comment = Comment.objects.create(post=post, body='this is just a comment',user=comment_user)

        self.assertEqual(str(comment), 'ana')
