# Generated by Django 3.1.4 on 2021-02-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0010_auto_20210108_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
