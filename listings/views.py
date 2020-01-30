from django.shortcuts import render
from django.utils.text import slugify

# Create your views here.

def listings(request):
    print("Listings: ", request.path)
    return render(request, 'listings/listings.html')

def listing(request, listing_slug):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')