# Generated by Django 4.1.2 on 2022-12-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
