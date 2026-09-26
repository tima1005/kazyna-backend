from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("gift", "Белек наборлор"),
        ("baby", "Бөбөк"),
        ("maternity", "Роддом"),
        ("prayer_mat", "Жайнамаз"),
        ("namaznik", "Намазник"),
        ("box", "Даяр бокстор"),
    ]

    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Фото"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name