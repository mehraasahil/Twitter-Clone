# Generated by Django 4.0.6 on 2022-08-12 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_like_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='like',
        ),
    ]