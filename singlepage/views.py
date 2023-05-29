from django.shortcuts import render

from slider.models import SliderItem
from .models import SinglePage


def single_page(request):
    page = SinglePage.objects.first()  # Or retrieve a specific page based on some criteria
    slider_items = SliderItem.objects.all()  # Retrieve all slider items
    return render(request, 'singlepage/body.html', {'page': page, 'slider_items': slider_items})
