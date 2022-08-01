from django.db import models
from account_engine.models import Profile

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    detail = models.TextField()
    image = models.ImageField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user
