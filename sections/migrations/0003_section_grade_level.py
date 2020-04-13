# Generated by Django 3.0.4 on 2020-04-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20200413_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='grade_level',
            field=models.CharField(blank=True, choices=[('NGSP', 'Non-graded SPED'), ('SP', 'SPED'), ('ALS', 'ALT LEARNING SYSTEM'), ('NU', 'NURSERY'), ('K', 'Kindergarten'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'Grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5'), ('G6', 'Grade 6')], max_length=60, null=True),
        ),
    ]
