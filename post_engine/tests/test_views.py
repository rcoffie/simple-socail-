from django.test import TestCase
from post_engine.models import Post, Comment
from django.urls import reverse
from django.contrib.auth.models import User

# class TestStudentContactForm(TestCase):
#     def test_can_send_message(self):
#         data = {
#             "first_name": "Juliana",
#             "last_name": " Crain",
#             "message": "Would love to talk about Philip K. Dick",
#         }
#         response = self.client.post("/contact/", data=data)
#         self.assertEqual(Contact.objects.count(), 1)
#         self.assertRedirects(response, "/thanks/")


class TestPostView(TestCase):
    def test_post_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'index.html')

class TestCreatePostView(TestCase):
    user1 = User.objects.create_user('man','password')
    def test_create_post(self):
        data = {
         "post":"this is the post",
         "user":user1,

        }
