# Generated by Django 5.0.6 on 2024-06-09 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_here',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='crated_on',
            new_name='show_time',
        ),
    ]
