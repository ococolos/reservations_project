# Generated by Django 3.0.10 on 2021-07-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commision_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
