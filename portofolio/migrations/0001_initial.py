# Generated by Django 5.0.2 on 2024-02-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Experience",
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
                ("company_logo", models.ImageField(upload_to="images/")),
                ("company_name", models.CharField(max_length=150)),
                ("job_title", models.CharField(max_length=150)),
                ("job_type", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("skills", models.JSONField()),
            ],
        ),
    ]