# Generated by Django 5.0 on 2023-12-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0015_coin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='importer',
            name='errors',
            field=models.TextField(blank=True, null=True),
        ),
    ]
