# Generated by Django 4.0.5 on 2022-06-04 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]