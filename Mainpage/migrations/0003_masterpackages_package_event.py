# Generated by Django 4.1.7 on 2023-02-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0002_rename_img_path_masterpackages_max_altitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterpackages',
            name='package_event',
            field=models.TextField(default='', max_length=100),
        ),
    ]
