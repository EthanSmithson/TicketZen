# Generated by Django 5.0.6 on 2024-07-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_recentsearch_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentsearch',
            name='departureDate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='recentsearch',
            name='returnDate',
            field=models.CharField(default='', max_length=100),
        ),
    ]