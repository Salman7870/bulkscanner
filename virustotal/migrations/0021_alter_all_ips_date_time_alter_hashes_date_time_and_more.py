# Generated by Django 4.1.1 on 2022-10-06 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0020_alter_all_ips_date_time_alter_hashes_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 42, 44, 80556)),
        ),
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 42, 44, 81516)),
        ),
        migrations.AlterField(
            model_name='malicious_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 14, 42, 44, 81516)),
        ),
    ]
