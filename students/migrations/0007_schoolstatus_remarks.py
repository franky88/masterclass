# Generated by Django 3.0.4 on 2020-04-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20200415_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolstatus',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]