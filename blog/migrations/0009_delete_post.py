# Generated by Django 4.1.2 on 2022-12-12 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]