# Generated by Django 3.2 on 2021-04-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20210421_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='coin',
            field=models.CharField(default='Dollar', max_length=20, null=True),
        ),
    ]
