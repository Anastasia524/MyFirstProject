# Generated by Django 4.1.2 on 2022-12-11 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_buytyr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buytyr',
            old_name='title',
            new_name='title1',
        ),
    ]