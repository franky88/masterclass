# Generated by Django 3.0.4 on 2020-04-16 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0006_auto_20200415_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='max_number',
        ),
        migrations.RemoveField(
            model_name='section',
            name='student_counter',
        ),
    ]
