# Generated by Django 4.1 on 2022-08-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_engine', '0012_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]