from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import uuid
from datetime import datetime
now = datetime.now()
from django.urls import reverse
import time
t = time.time()
import random
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    slug = models.SlugField(max_length=250,  blank=True)
    image = models.ImageField(upload_to = 'post_images', blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_on =  models.DateTimeField(auto_now_add=True)


    def get_total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.user.username



    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)  + "-" + slugify(t)  + "-" + slugify(random.randint(0,1000))
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.user)  + "-" + slugify(t)  + "-" + slugify(random.randint(0,1000))
            self.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body= models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('edit_comment', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)  + "-" + slugify(self.date) + "-" + slugify(self.post.id)
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.user.username)  + "-" + slugify(self.date) + "-" + slugify(self.post.id)
            self.save()
