# Generated by Django 4.1.1 on 2022-10-03 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virustotal', '0010_alter_all_ips_date_time_alter_hashes_copyright_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='failed_scanned_hash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.TextField(unique=True)),
                ('error', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='all_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 19, 13, 14, 523357)),
        ),
        migrations.AlterField(
            model_name='hashes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 19, 13, 14, 523357)),
        ),
        migrations.AlterField(
            model_name='malicious_ips',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 19, 13, 14, 523357)),
        ),
    ]
