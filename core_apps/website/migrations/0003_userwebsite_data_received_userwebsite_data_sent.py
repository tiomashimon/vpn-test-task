# Generated by Django 4.2.5 on 2023-12-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_userwebsite_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwebsite',
            name='data_received',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='userwebsite',
            name='data_sent',
            field=models.FloatField(default=0),
        ),
    ]
