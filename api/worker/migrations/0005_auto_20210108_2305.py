# Generated by Django 3.0.11 on 2021-01-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20210108_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='/static/default.png', null=True, upload_to='images/'),
        ),
    ]
