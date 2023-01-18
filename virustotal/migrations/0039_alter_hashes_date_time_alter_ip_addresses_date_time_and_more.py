# Generated by Django 4.1.1 on 2022-12-23 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0038_alter_hashes_date_time_alter_ip_addresses_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 20, 22, 38, 833367)),
        ),
        migrations.AlterField(
            model_name='ip_addresses',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 20, 22, 38, 833367)),
        ),
        migrations.AlterField(
            model_name='ip_addresses',
            name='network',
            field=models.CharField(max_length=100, null=True),
        ),
    ]