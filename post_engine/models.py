from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    image = models.ImageField(upload_to = 'post_images', blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username