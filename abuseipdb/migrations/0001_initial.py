# Generated by Django 4.1.1 on 2022-10-10 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip_addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, unique=True)),
                ('isPublic', models.CharField(max_length=10)),
                ('ipVersion', models.IntegerField(null=True)),
                ('isWhitelisted', models.BooleanField()),
                ('abuseConfidenceScore', models.IntegerField(null=True)),
                ('countryCode', models.CharField(max_length=5, null=True)),
                ('usageType', models.TextField(null=True)),
                ('isp', models.TextField(null=True)),
                ('domain', models.TextField(null=True)),
                ('totalReports', models.IntegerField(null=True)),
                ('numDistinctUsers', models.IntegerField(null=True)),
                ('lastReportedAt', models.DateTimeField()),
                ('hostnames', models.JSONField(null=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2022, 10, 10, 16, 20, 50, 436781))),
            ],
        ),
    ]