# Generated by Django 4.0.5 on 2022-06-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
