# Generated by Django 3.0.4 on 2020-04-13 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20200413_1115'),
        ('students', '0002_auto_20200413_1115'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentSchedule',
        ),
    ]
