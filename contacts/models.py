from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    listing_slug = models.SlugField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


    # def save(self, *args, **kwargs):
    #     if not self.listing_slug:
    #         self.listing_slug = slugify(self.listing)
    #         super(Contact, self).save(*args, *args, **kwargs)


