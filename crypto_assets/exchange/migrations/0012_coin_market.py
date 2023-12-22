# Generated by Django 5.0 on 2023-12-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0011_transaction_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='market',
            field=models.CharField(choices=[('irt', 'irt'), ('usdt', 'usdt')], max_length=10, null=True),
        ),
    ]