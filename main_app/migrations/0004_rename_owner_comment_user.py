# Generated by Django 4.0.3 on 2022-03-09 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0003_remove_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='user',
        ),
    ]
