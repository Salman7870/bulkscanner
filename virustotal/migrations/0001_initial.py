# Generated by Django 4.1.1 on 2022-09-22 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_ips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, unique=True)),
                ('count', models.IntegerField(null=True)),
                ('harmless_votes', models.IntegerField(null=True)),
                ('malicious_votes', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=5, null=True)),
                ('abuse_confidence_Score', models.IntegerField(null=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2022, 9, 22, 13, 3, 40, 532672))),
            ],
        ),
        migrations.CreateModel(
            name='malicious_ips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, unique=True)),
                ('count', models.IntegerField(null=True)),
                ('harmless_votes', models.IntegerField(null=True)),
                ('malicious_votes', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=5)),
                ('abuse_confidence_Score', models.IntegerField(null=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2022, 9, 22, 13, 3, 40, 532672))),
            ],
        ),
    ]
