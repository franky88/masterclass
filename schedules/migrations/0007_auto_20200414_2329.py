# Generated by Django 3.0.4 on 2020-04-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_auto_20200414_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]