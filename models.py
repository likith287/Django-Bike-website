from django.db import models

class Bike(models.Model):
    CATEGORY_CHOICES = [
        ("Sports", "Sports"),
        ("Cruiser", "Cruiser"),
        ("Adventure", "Adventure"),
        ("Commuter", "Commuter"),
    ]
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Sports")
    price = models.PositiveIntegerField(help_text="Price in Indian rupees")
    engine_cc = models.PositiveIntegerField(default=150, verbose_name="Engine (cc)")
    description = models.TextField()
    image_url = models.URLField(blank=True, help_text="Optional image URL")
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-featured", "price"]

    def __str__(self):
        return f"{self.brand} {self.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
