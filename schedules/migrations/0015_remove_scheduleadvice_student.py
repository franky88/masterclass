# Generated by Django 3.0.4 on 2020-04-17 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0014_auto_20200417_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleadvice',
            name='student',
        ),
    ]
