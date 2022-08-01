from email.policy import default
from django.db import models
from account_engine.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.TextField()
    image = models.ImageField(upload_to="post_images", default="default.webg")
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail
