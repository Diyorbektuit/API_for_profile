# Generated by Django 5.0.3 on 2024-04-23 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='auther',
            new_name='author',
        ),
    ]
