# Generated by Django 2.0.6 on 2018-08-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180827_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar_photos/avatar-159236_1280.png', upload_to='avatar_photos'),
        ),
    ]
