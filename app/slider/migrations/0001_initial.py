from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("filer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SliderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("order", models.PositiveIntegerField(db_index=True, default=0, verbose_name="Порядок")),
                ("is_active", models.BooleanField(default=True, verbose_name="Показывать")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Создано")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлено")),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="slider_items",
                        to="filer.image",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Слайд",
                "verbose_name_plural": "Слайды",
                "ordering": ("order", "id"),
            },
        ),
    ]
