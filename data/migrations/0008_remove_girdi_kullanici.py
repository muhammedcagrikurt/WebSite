# Generated by Django 4.0 on 2022-01-05 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_girdi_kullanici'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='girdi',
            name='kullanici',
        ),
    ]
