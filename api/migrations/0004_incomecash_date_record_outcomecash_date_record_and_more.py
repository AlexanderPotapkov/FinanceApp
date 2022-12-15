# Generated by Django 4.1.3 on 2022-12-14 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_incomecash_date_alter_outcomecash_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomecash',
            name='date_record',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 10, 24, 6, 166080), verbose_name='Дата записи'),
        ),
        migrations.AddField(
            model_name='outcomecash',
            name='date_record',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 10, 24, 6, 166080), verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='incomecash',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='outcomecash',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи'),
        ),
    ]
