# Generated by Django 3.2.5 on 2021-07-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_boards', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
