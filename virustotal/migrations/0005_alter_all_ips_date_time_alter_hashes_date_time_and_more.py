# Generated by Django 4.1.1 on 2022-09-30 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0004_hashes_alter_all_ips_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 20, 9, 3, 611449)),
        ),
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 20, 9, 3, 611449)),
        ),
        migrations.AlterField(
            model_name='malicious_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 20, 9, 3, 611449)),
        ),
    ]