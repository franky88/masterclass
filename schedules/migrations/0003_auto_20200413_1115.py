# Generated by Django 3.0.4 on 2020-04-13 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20200412_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentschedule',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='studentschedule',
            name='user',
        ),
    ]
