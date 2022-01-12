# Generated by Django 3.2.9 on 2022-01-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_rename_coin_market'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Market',
        ),
    ]
