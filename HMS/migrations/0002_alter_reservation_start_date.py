# Generated by Django 4.0.4 on 2022-06-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Start_date',
            field=models.CharField(max_length=100),
        ),
    ]