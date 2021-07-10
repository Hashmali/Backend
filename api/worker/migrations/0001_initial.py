# Generated by Django 3.0.11 on 2021-07-10 16:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id_img', models.URLField(default='')),
                ('first_name', models.CharField(default='worker', max_length=50)),
                ('second_name', models.CharField(default='worker', max_length=50)),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='wrong Phone number', regex='^[0][5][0|2|3|4|5|6|9]{1}[-]{0,1}[0-9]{7}$')])),
                ('id_no', models.CharField(blank=True, max_length=10, null=True)),
                ('driving_license_img', models.URLField(default='')),
                ('work_license_israel', models.CharField(blank=True, max_length=50, null=True)),
                ('work_license_type', models.CharField(blank=True, max_length=50, null=True)),
                ('work_license_expire', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('pay_per_day', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.URLField(default='https://res.cloudinary.com/dj42j4pqu/image/upload/v1619305524/plfj8pvkj9pizrv9to57.png')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('phone',),
            },
        ),
    ]
