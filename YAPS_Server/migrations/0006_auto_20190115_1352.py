# Generated by Django 2.0.3 on 2019-01-15 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAPS_Server', '0005_auto_20190115_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pickupTime',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
