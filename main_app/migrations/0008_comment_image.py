# Generated by Django 4.0.3 on 2022-03-13 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0007_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
