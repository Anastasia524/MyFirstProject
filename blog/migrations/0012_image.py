# Generated by Django 4.1.2 on 2022-12-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_comment_remove_comments_post_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
