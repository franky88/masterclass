# Generated by Django 3.0.4 on 2020-04-17 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200417_1006'),
        ('schedules', '0013_scheduleadvice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleadvice',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.Schedule'),
        ),
        migrations.AlterField(
            model_name='scheduleadvice',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.StudentName'),
        ),
    ]
