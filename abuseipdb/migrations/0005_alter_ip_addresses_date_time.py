# Generated by Django 4.1.1 on 2022-12-23 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abuseipdb', '0004_alter_ip_addresses_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_addresses',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 20, 22, 38, 835992)),
        ),
    ]
