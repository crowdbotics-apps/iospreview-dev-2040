# Generated by Django 2.2.11 on 2020-03-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='bdd',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
