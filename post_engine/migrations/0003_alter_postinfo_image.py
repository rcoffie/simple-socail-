# Generated by Django 4.0.6 on 2022-08-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_engine', '0002_alter_postinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postinfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
    ]