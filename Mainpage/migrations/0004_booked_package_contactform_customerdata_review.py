# Generated by Django 4.1.7 on 2023-02-17 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainpage', '0003_masterpackages_package_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked_package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.IntegerField(default=0)),
                ('customer_id', models.IntegerField(default=0)),
                ('payment_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(default='', max_length=100)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(default=0)),
                ('customer_name', models.TextField(default='', max_length=100)),
                ('customer_address', models.TextField(default='', max_length=100)),
                ('customer_mobile', models.TextField(default='', max_length=100)),
                ('customer_email', models.TextField(default='', max_length=100)),
                ('customer_gender', models.TextField(default='', max_length=100)),
                ('customer_dob', models.DateField(default=datetime.date.today)),
                ('customer_img', models.ImageField(upload_to='myprofile')),
                ('customer_package_id', models.TextField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(default=0)),
                ('stars', models.IntegerField(default=0)),
                ('review_text', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
