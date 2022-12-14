# Generated by Django 4.1.3 on 2022-12-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnerAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_one', models.ImageField(upload_to='media')),
                ('ad_two', models.ImageField(blank=True, null=True, upload_to='media')),
                ('ad_three', models.ImageField(blank=True, null=True, upload_to='media')),
                ('active', models.BooleanField(default=True)),
                ('ad_one_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_two_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_three_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasterAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_one', models.ImageField(upload_to='media')),
                ('ad_two', models.ImageField(blank=True, null=True, upload_to='media')),
                ('ad_three', models.ImageField(blank=True, null=True, upload_to='media')),
                ('active', models.BooleanField(default=True)),
                ('ad_one_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_two_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_three_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecondAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_one', models.ImageField(upload_to='media')),
                ('ad_two', models.ImageField(blank=True, null=True, upload_to='media')),
                ('ad_three', models.ImageField(blank=True, null=True, upload_to='media')),
                ('active', models.BooleanField(default=True)),
                ('ad_one_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_two_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_three_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThirdAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_one', models.ImageField(upload_to='media')),
                ('ad_two', models.ImageField(blank=True, null=True, upload_to='media')),
                ('ad_three', models.ImageField(blank=True, null=True, upload_to='media')),
                ('active', models.BooleanField(default=True)),
                ('ad_one_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_two_link', models.CharField(blank=True, max_length=200, null=True)),
                ('ad_three_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
