# Generated by Django 4.1.7 on 2023-02-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0004_booked_package_contactform_customerdata_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewer_name',
            field=models.TextField(default='', max_length=200),
        ),
    ]
