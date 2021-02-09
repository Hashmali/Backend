# Generated by Django 3.0.11 on 2020-12-26 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20201226_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='project_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='project.Project'),
        ),
    ]
