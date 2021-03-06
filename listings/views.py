from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Listing
# for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from realtors.models import Realtor
from .choices import state_choices, bedroom_choices, price_choices


def listings(request):
    # print('****************listings called**************')
    # print("Listings: ", request.path)
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    listings_paged = paginator.get_page(page)
    # filter the published listings
    # listings_published = [listing for listing in listings_paged if listing.is_published]
    data = {
        'listings': listings_paged
    }
    return render(request, 'listings/listings.html', data)


def listing(request, listing_slug):
    # print('****************listing called**************')
    listing = get_object_or_404(Listing, slug=listing_slug)
    seller_of_month = Realtor.objects.filter(is_mvp=True)
    # print(seller_of_month)
    data = {
        'listing': listing,
        'seller_of_month': seller_of_month
    }
    return render(request, 'listings/listing.html', data)


def search(request):
    # print('****************search called**************')
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # use contains for case sensitive not icontains
    
    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # use exact for case sensitive not iexact
    
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) # use exact for case sensitive not iexact

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # use exact for case sensitive not iexact

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        print(price)
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # use exact for case sensitive not iexact

    data = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request, 'listings/search.html', data)
