# Generated by Django 5.0 on 2023-12-11 03:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_rename_date_transaction_jdate'),
        ('notification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('status', models.CharField(blank=True, choices=[('upper', 'upper'), ('lower', 'lower')], max_length=10, null=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='exchange.coin')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
