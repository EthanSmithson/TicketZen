# Generated by Django 5.0.6 on 2024-07-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_user_activateuuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='savedTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=10)),
                ('ticket', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
