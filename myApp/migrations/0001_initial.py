# Generated by Django 4.2.13 on 2024-05-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='N/A', max_length=100)),
                ('lastName', models.CharField(default='N/A', max_length=100)),
                ('username', models.CharField(default='N/A', max_length=12)),
                ('password', models.CharField(default='N/A', max_length=12)),
            ],
        ),
    ]
