# Generated by Django 5.0 on 2023-12-22 14:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_notification_transaction_alter_notification_coin'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
