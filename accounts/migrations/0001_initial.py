# Generated by Django 2.0.6 on 2018-08-27 23:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('birth_date', models.DateField(blank=True)),
                ('bio', models.TextField(blank=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar_photos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
