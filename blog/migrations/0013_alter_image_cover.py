# Generated by Django 4.1.2 on 2022-12-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='cover',
            field=models.ImageField(upload_to='images'),
        ),
    ]