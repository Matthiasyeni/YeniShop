# Generated by Django 4.2.11 on 2024-04-15 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import store.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ("slug", models.CharField(max_length=50, verbose_name="Slug")),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to=store.models.get_file_path,
                        verbose_name="Image",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Description"),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=False,
                        help_text="0=default, 1=Hidden",
                        verbose_name="Status",
                    ),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False,
                        help_text="0=default, 1=Trending",
                        verbose_name="Trending",
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(max_length=150, verbose_name="Meta Title"),
                ),
                (
                    "meta_keywords",
                    models.CharField(max_length=150, verbose_name="Meta Keywords"),
                ),
                (
                    "meta_description",
                    models.CharField(max_length=500, verbose_name="Meta Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Created At"
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="ContactUser",
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
                ("firstname", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=50)),
                ("subject", models.TextField(max_length=550)),
                ("city", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("fname", models.CharField(max_length=150)),
                ("lname", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=150)),
                ("address", models.TextField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                ("total_price", models.FloatField()),
                ("payment_mode", models.CharField(max_length=150)),
                ("payment_id", models.CharField(max_length=250)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Out For Shipping", "Out For Shipping"),
                            ("Completed", "Completed"),
                        ],
                        default="Pending",
                        max_length=150,
                    ),
                ),
                ("message", models.CharField(max_length=150)),
                ("tracking_no", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
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
                ("slug", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                (
                    "product_image",
                    models.ImageField(blank=True, upload_to=store.models.get_file_path),
                ),
                ("small_description", models.CharField(max_length=250)),
                ("quantity", models.PositiveIntegerField()),
                ("description", models.TextField(max_length=500)),
                ("original_price", models.FloatField()),
                ("selling_price", models.FloatField()),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0=default, 1=Hidden"),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False, help_text="0=default, 1=Trending"
                    ),
                ),
                ("tag", models.CharField(max_length=50)),
                ("meta_title", models.CharField(max_length=150)),
                ("meta_keywords", models.CharField(max_length=150)),
                ("meta_description", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("phone", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("product_qty", models.IntegerField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]