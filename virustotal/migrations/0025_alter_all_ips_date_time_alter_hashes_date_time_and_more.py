# Generated by Django 4.1.1 on 2022-10-06 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0024_alter_all_ips_date_time_alter_hashes_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 3, 7, 479483)),
        ),
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 3, 7, 480480)),
        ),
        migrations.AlterField(
            model_name='malicious_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 3, 7, 479483)),
        ),
    ]
