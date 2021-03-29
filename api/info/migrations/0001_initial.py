# Generated by Django 3.0.11 on 2021-03-28 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_no', models.CharField(max_length=100, null=True)),
                ('license_expiry_date', models.DateTimeField()),
                ('insurance_expiry_date', models.DateTimeField()),
                ('insurance_age', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('car', models.ManyToManyField(blank=True, to='info.Car')),
                ('deputy_director', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deputy_director', to=settings.AUTH_USER_MODEL)),
                ('manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
