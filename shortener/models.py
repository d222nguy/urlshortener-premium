from django.db import models
from .utils import code_generator, create_shortcode, addHttpIfNecessary
from django.conf import settings
from .validators import validate_url
from django_hosts.resolvers import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(URLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active = True)
        return qs
    def refresh_shortcode(self, items = None):
        print(items)
        #qs: query set
        qs = URL.objects.filter(id__gte = 1) #id >= 1, every items!
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i = new_codes)
class URL(models.Model):
    url = models.CharField(max_length = 220, validators = [validate_url])
    shortcode = models.CharField(max_length = SHORTCODE_MAX, null = False, blank = True, unique = True)
    timestamp = models.DateTimeField(auto_now_add = True) 
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    #Override Django "objects"
    objects = URLManager()

    some_random = URLManager()
    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
    def save(self, *args, **kwargs):
        self.url = addHttpIfNecessary(self.url)
        if not self.shortcode or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(URL, self).save(*args, **kwargs)
    def get_short_url(self):
        print("self.shortcode = ", self.shortcode)
        return self.shortcode
    