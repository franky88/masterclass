# Generated by Django 3.0.4 on 2020-04-20 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20200417_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentname',
            name='advice',
        ),
        migrations.RemoveField(
            model_name='studentname',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='studentname',
            name='schedule',
        ),
    ]
