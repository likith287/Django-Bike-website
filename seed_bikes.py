from django.core.management.base import BaseCommand
from bikes.models import Bike

SAMPLE_BIKES = [
    {"name":"Street 200","brand":"Apex","category":"Sports","price":185000,"engine_cc":200,"featured":True,
     "description":"A sharp, lightweight street bike made for everyday rides and weekend escapes.",
     "image_url":"https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=85"},
    {"name":"Classic 350","brand":"Roadcraft","category":"Cruiser","price":210000,"engine_cc":350,"featured":True,
     "description":"Classic styling, relaxed ergonomics, and a comfortable riding position for longer journeys.",
     "image_url":"https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1200&q=85"},
    {"name":"Trail X","brand":"Summit","category":"Adventure","price":245000,"engine_cc":250,"featured":True,
     "description":"An adventure-inspired motorcycle for city streets and carefully planned road trips.",
     "image_url":"https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=85"},
    {"name":"City 125","brand":"Apex","category":"Commuter","price":95000,"engine_cc":125,
     "description":"A practical commuter with an approachable engine size and a simple, clean design.",
     "image_url":"https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1200&q=85"},
    {"name":"Racer 300","brand":"Velocity","category":"Sports","price":275000,"engine_cc":300,
     "description":"A sporty profile and focused road manners for riders who enjoy a dynamic look.",
     "image_url":"https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=85"},
    {"name":"Tourer 400","brand":"Roadcraft","category":"Cruiser","price":320000,"engine_cc":400,
     "description":"A road-oriented touring option with a broad seat and a relaxed riding character.",
     "image_url":"https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1200&q=85"},
]

class Command(BaseCommand):
    help = "Add sample bikes to the database"

    def handle(self, *args, **options):
        created = 0
        for item in SAMPLE_BIKES:
            _, was_created = Bike.objects.get_or_create(
                brand=item["brand"], name=item["name"], defaults=item
            )
            created += int(was_created)
        self.stdout.write(self.style.SUCCESS(f"Sample bikes ready. Added {created} new bike(s)."))
