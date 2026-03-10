from django.shortcuts import render

from .models import SliderItem


def slider_page(request):
    slides = SliderItem.objects.filter(is_active=True).order_by("order", "id")
    return render(request, "slider/index.html", {"slides": slides})
