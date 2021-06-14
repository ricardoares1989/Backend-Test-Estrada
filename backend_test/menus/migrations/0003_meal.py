# Generated by Django 3.0.8 on 2021-06-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0002_auto_20210614_0200"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meal",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date time on which the object was created.",
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Date time on which the object was modified",
                        verbose_name="updated at",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField()),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "get_latest_by": "created_at",
                "abstract": False,
            },
        ),
    ]
