import uuid
from django.db import models
from django.core.validators import MinValueValidator

QUANTITY_TYPES = (
    ("nos", "Numbers"),
    ("ltr", "Litres"),
    ("mtr", "Meters"),
    ("cm", "Centimeters"),
    ("mm", "Millimeters"),
    ("kgs", "Kilograms"),
    ("pcs", "Pieces"),
    ("ft", "Feet"),
    ("sqft", "SquareFeet"),
)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Item(BaseModel):
    """Represent a single item in inventory"""
    name = models.CharField(
        max_length=100,
        help_text="Enter Item Name (e.g. Laminate Sheet)",
        verbose_name="Item Name",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0, message="Quantity must alteast be zero!")
        ],
        verbose_name="Item Quantity",
    )
    minimum_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Item Minimum Quantity",
    )
    quantity_type = models.CharField(
        max_length=20,
        choices=QUANTITY_TYPES,
        default="nos",
        verbose_name="Item Quantity Type",
    )

    class Meta:
        ordering = ['-name']

    def __str__(self):
        """string representation of an item"""
        return self.name