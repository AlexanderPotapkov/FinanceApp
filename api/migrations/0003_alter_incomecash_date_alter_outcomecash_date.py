# Generated by Django 4.1.3 on 2022-12-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_categories_income_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomecash',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='outcomecash',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
    ]
