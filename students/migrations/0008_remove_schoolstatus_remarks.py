# Generated by Django 3.0.4 on 2020-04-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_schoolstatus_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolstatus',
            name='remarks',
        ),
    ]
