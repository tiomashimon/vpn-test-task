# Generated by Django 4.2.5 on 2023-12-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_userwebsite_data_received_userwebsite_data_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwebsite',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
