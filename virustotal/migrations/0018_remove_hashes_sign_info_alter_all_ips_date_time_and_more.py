# Generated by Django 4.1.1 on 2022-10-06 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0017_alter_all_ips_date_time_alter_hashes_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashes',
            name='sign_info',
        ),
        migrations.AlterField(
            model_name='all_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 34, 11, 923007)),
        ),
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 34, 11, 924056)),
        ),
        migrations.AlterField(
            model_name='malicious_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 34, 11, 924056)),
        ),
    ]
