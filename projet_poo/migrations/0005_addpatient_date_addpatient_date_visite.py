# Generated by Django 4.0.5 on 2023-01-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet_poo', '0004_auto_20230122_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpatient',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='addpatient',
            name='date_visite',
            field=models.DateField(null=True),
        ),
    ]