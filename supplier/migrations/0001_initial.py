# Generated by Django 5.1 on 2024-08-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_manufactural", models.BooleanField()),
                ("supplier_name", models.CharField(max_length=50)),
                ("supplier_phone", models.CharField(max_length=50)),
            ],
        ),
    ]
