# Generated by Django 4.1.1 on 2023-01-03 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abuseipdb', '0008_alter_ip_addresses_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_addresses',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 18, 1, 4, 960735)),
        ),
    ]
