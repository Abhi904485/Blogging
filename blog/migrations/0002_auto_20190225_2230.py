# Generated by Django 2.2b1 on 2019-02-25 22:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date_posted',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]
