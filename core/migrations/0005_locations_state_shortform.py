# Generated by Django 4.0.10 on 2023-06-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='state_shortform',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
