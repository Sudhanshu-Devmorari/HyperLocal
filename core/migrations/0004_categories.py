# Generated by Django 4.0.10 on 2023-06-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_locations_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_name', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]