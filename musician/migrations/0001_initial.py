# Generated by Django 5.0.6 on 2024-06-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_no', models.CharField(max_length=12)),
                ('Instrument_Type', models.CharField(max_length=50)),
            ],
        ),
    ]