from django.db import models
from django.utils.text import slugify
from realtors.models import Realtor
from datetime import datetime
import arrow
import humanize

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, )
    title = models.CharField(max_length=200, blank=False, unique=False)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, *args, **kwargs)

    def list_date_preety(self):
        return self.list_date.strftime("%Y-%m-%d")

    def list_date_humanized(self):
        listed_date = arrow.get(self.list_date)
        return listed_date.humanize()

    def price_humanized(self):
        return humanize.intword(self.price)

    def price_commaed(self):
        return humanize.intcomma(self.price)

    class Meta:
        ordering = ('-list_date',)


        

