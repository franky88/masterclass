# Generated by Django 3.0.4 on 2020-04-22 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0007_auto_20200416_2251'),
        ('schedules', '0018_studentadviceschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=120)),
                ('max_number', models.IntegerField(default=0, verbose_name='maximum number of students')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.Section')),
            ],
        ),
        migrations.AlterField(
            model_name='studentadviceschedule',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.SubjectSchedule'),
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
