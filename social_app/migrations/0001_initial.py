# Generated by Django 4.0.6 on 2022-08-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.TextField()),
                ('image', models.ImageField(default='default.webg', upload_to='post_images')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
