# Generated by Django 2.0.6 on 2018-09-04 23:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180904_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
    ]
