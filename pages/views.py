from django.shortcuts import render
from listings.models import Listing


def home(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    data = {
        'listings': latest_listings
    }
    return render(request, 'pages/index.html', data)


def about(request):
    return render(request, 'pages/about.html')
