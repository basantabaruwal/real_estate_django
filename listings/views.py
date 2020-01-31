from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Listing
# for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from realtors.models import Realtor


def listings(request):
    print('****************listings called**************')
    # print("Listings: ", request.path)
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    listings_paged = paginator.get_page(page)
    # filter the published listings
    # listings_published = [listing for listing in listings_paged if listing.is_published]
    data = {
        'listings': listings_paged
    }
    return render(request, 'listings/listings.html', data)


def listing(request, listing_slug):
    print('****************listing called**************')
    listing = get_object_or_404(Listing, slug=listing_slug)
    seller_of_month = Realtor.objects.filter(is_mvp=True)
    # print(seller_of_month)
    data = {
        'listing': listing,
        'seller_of_month': seller_of_month
    }
    return render(request, 'listings/listing.html', data)


def search(request):
    print('****************search called**************')
    return render(request, 'listings/search.html')
