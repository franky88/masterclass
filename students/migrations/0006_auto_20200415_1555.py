# Generated by Django 3.0.4 on 2020-04-15 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20200415_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolstatus',
            options={'verbose_name_plural': 'school statuses'},
        ),
    ]