# Generated by Django 4.0.10 on 2023-06-02 06:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=512, null=True)),
                ('cities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=512, null=True), default=list, size=None)),
            ],
        ),
    ]
