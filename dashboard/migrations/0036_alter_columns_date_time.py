# Generated by Django 4.1.1 on 2022-12-23 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_alter_columns_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columns',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 23, 20, 22, 38, 838038)),
        ),
    ]
