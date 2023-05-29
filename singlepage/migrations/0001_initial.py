# Generated by Django 4.2.1 on 2023-05-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SinglePage",
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
                ("title", models.CharField(max_length=200)),
                ("seo_title", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "seo_description",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "seo_keywords",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("body", models.TextField()),
            ],
        ),
    ]
