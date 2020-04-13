# Generated by Django 3.0.4 on 2020-04-13 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20200413_1115'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentname',
            name='advice',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentname',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentname',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.Schedule'),
        ),
    ]
