# Generated by Django 5.0.4 on 2024-04-29 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pat1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_name',
            name='gmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pat1.student_login'),
        ),
    ]
