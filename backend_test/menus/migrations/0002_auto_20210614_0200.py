# Generated by Django 3.0.8 on 2021-06-14 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menu",
            old_name="specific_date",
            new_name="date",
        ),
    ]
