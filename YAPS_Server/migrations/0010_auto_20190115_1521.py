# Generated by Django 2.0.3 on 2019-01-15 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAPS_Server', '0009_auto_20190115_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='threshold',
        ),
        migrations.AlterField(
            model_name='group',
            name='pickupTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]