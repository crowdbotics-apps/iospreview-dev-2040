# Generated by Django 2.2.11 on 2020-03-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200318_1218"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
