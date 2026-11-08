from django.contrib import admin
from .models import Bike, ContactMessage

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "price", "engine_cc", "featured")
    list_filter = ("category", "brand", "featured")
    search_fields = ("name", "brand")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    readonly_fields = ("created_at",)
