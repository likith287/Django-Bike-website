from django.contrib import admin
from django.urls import path
from bikes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("bikes/", views.bike_list, name="bike_list"),
    path("bikes/<int:pk>/", views.bike_detail, name="bike_detail"),
    path("contact/", views.contact, name="contact"),
]
