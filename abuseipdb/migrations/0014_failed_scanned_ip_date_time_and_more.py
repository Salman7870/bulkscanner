# Generated by Django 4.1.1 on 2023-03-01 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abuseipdb', '0013_alter_ip_addresses_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='failed_scanned_ip',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 19, 48, 45, 989378)),
        ),
        migrations.AlterField(
            model_name='ip_addresses',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 19, 48, 45, 988333)),
        ),
    ]
