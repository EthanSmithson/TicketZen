# Generated by Django 5.0.6 on 2024-07-12 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_savedticket_zerosecondflightdeparturedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedticket',
            name='zeroSecondFlightDepartureDate',
        ),
    ]