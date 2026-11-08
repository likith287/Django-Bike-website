from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import Bike

def home(request):
    featured_bikes = Bike.objects.filter(featured=True)[:3]
    if not featured_bikes.exists():
        featured_bikes = Bike.objects.all()[:3]
    return render(request, "bikes/home.html", {"featured_bikes": featured_bikes})

def bike_list(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    bikes = Bike.objects.all()
    if query:
        bikes = bikes.filter(Q(name__icontains=query) | Q(brand__icontains=query) | Q(description__icontains=query))
    if category:
        bikes = bikes.filter(category=category)
    return render(request, "bikes/bike_list.html", {
        "bikes": bikes, "query": query, "selected_category": category,
        "categories": Bike.CATEGORY_CHOICES,
    })

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, "bikes/bike_detail.html", {"bike": bike})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thanks! Your message has been sent.")
        return redirect("contact")
    return render(request, "bikes/contact.html", {"form": form})
