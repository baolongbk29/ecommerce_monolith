# Generated by Django 4.1.13 on 2023-12-04 10:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="state",
            name="country",
        ),
        migrations.DeleteModel(
            name="City",
        ),
        migrations.DeleteModel(
            name="Country",
        ),
        migrations.DeleteModel(
            name="State",
        ),
    ]
