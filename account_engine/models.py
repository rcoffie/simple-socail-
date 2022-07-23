from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # photo = models.ImageField(upload_to='users/%Y/%m/%d/',
    # blank=True)

    def __str__(self):
        return f"Profile for user {self.user.username}"
