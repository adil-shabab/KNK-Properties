# Generated by Django 4.1.3 on 2023-01-03 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_masterad_ad_one_status_masterad_ad_three_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterad',
            name='ad_one_status',
        ),
        migrations.RemoveField(
            model_name='masterad',
            name='ad_three_status',
        ),
        migrations.RemoveField(
            model_name='masterad',
            name='ad_two_status',
        ),
    ]
