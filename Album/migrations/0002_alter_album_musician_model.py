# Generated by Django 5.0.6 on 2024-06-17 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musician_model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='musician.musician'),
        ),
    ]
