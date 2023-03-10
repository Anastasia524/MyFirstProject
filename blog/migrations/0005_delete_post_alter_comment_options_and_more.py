# Generated by Django 4.1.2 on 2022-12-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
