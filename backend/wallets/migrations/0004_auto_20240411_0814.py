# Generated by Django 3.2 on 2024-04-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0003_auto_20240410_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='state',
            field=models.CharField(choices=[('created', 'created'), ('failed', 'failed'), ('done', 'done')], db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('deposit', 'deposit'), ('withdraw', 'withdraw')], db_index=True, max_length=10),
        ),
    ]