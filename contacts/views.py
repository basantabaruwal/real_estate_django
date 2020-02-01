from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from datetime import datetime
from django.contrib import messages
import json


def contact(request):
    print(json.dumps(request.POST))
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_name = request.POST['realtor_name']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, contact_date=datetime.now, user_id=user_id)

        try:
            contact.save()
            messages.success(
                request, "Thank you for your inquiry. Our realtor {} will contact you soon.".format(realtor_name))
        except:
            messages.error(
                request, "Sorry, Some error occurred. Please try again later")
        finally:
            # redirect to same page
            return redirect(request.META['HTTP_REFERER'])

    # redirect to same page
    return redirect(request.META['HTTP_REFERER'])
