# Generated by Django 3.2 on 2021-04-21 17:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='coin',
            field=models.CharField(default='Dollar', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(50)]),
        ),
    ]