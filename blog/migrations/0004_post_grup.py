# Generated by Django 4.0 on 2022-01-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grup',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('instagram', 'Instagram'), ('facebook', 'Facebook')], default='twiter', max_length=15),
        ),
    ]
