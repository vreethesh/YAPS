# Generated by Django 2.0.3 on 2019-01-14 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAPS_Server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='share',
            field=models.CharField(choices=[('E', 'Exclusive'), ('W', 'Willing'), ('N', 'Non Willing')], default='W', max_length=1),
        ),
    ]
