# Generated by Django 4.1 on 2022-08-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_engine', '0009_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
