# Generated by Django 4.2.14 on 2024-07-31 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="categories/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SocialMedia",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("facebook", "Facebook"),
                            ("twitter", "Twitter"),
                            ("instagram", "Instagram"),
                            ("linkedin", "Linkedin"),
                            ("youtube", "YouTube"),
                        ],
                        max_length=20,
                        unique=True,
                        verbose_name="Adı",
                    ),
                ),
                ("link", models.URLField(verbose_name="Bağlantı")),
            ],
            options={
                "verbose_name": "Sosyal Medya",
                "verbose_name_plural": "Sosyal Medya",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("ingredients", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="products/"),
                ),
                ("available", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="app.category",
                    ),
                ),
            ],
        ),
    ]
