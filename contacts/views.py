from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from datetime import datetime
from django.contrib import messages
import json
from django.core.mail import send_mail
from django.conf import settings


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
        # user_id = request.POST['user_id']

        # defult user_id
        user_id = 0

        # check if the inquiry is duplicate
        # current_user = request.user
        # print("Current User: ",current_user)
        # if user_id != '0':
        if request.user.is_authenticated:
            # user is authenticated
            user_id = request.user.id
            has_inquired = Contact.objects.filter(
                user_id=user_id, listing_id=listing_id).exists()
            if has_inquired:
                # duplicate inquiry
                messages.error(
                    request, "You've already made an inquiry for this property.")
                return redirect(request.META['HTTP_REFERER'])

        try:
            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                              phone=phone, message=message, user_id=user_id)

            try:
            # send the mail to corresponding realtor
                send_mail(
                    'Property Listing Inquiry',
                    'There has been an inquiry for '+ listing +'. Sign into the admin panel for more info.',
                    settings.EMAIL_HOST_USER,
                    [realtor_email, 'baruwalbasanta@gmail.com'],
                    fail_silently=False
                )
            except:
                # email couldn't be sent
                # messages.error(request, "Email couln't be sent to the realtor!!")
                pass
            
            # save the contact
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
