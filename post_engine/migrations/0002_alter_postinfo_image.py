# Generated by Django 4.0.6 on 2022-08-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinfo',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_images'),
        ),
    ]