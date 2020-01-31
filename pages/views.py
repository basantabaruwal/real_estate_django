from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def home(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    data = {
        'listings': latest_listings
    }
    return render(request, 'pages/index.html', data)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    seller_of_the_month = Realtor.objects.filter(is_mvp=True)
    data = {
        'realtors': realtors,
        'seller_of_the_month': seller_of_the_month
    }
    return render(request, 'pages/about.html', data)
