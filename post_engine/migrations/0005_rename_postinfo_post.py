# Generated by Django 4.1 on 2022-08-12 14:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_engine', '0004_alter_postinfo_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostInfo',
            new_name='Post',
        ),
    ]
