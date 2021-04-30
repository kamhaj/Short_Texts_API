from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


## one (user) to many (posts) relation
class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=160)       # unrestricted text
    creation_date = models.DateTimeField(default=timezone.now, editable=False) #
    edition_date = models.DateTimeField(blank=True, null=True)
    views_counter = models.IntegerField(default=0, null=True, blank=True)

    ## change publish date (e.g. on update)
    def update_edition_date(self):
        self.updated_date = timezone.now()
        self.save()

    ## update views counter by 1 each time it's being requested
    def update_views_counter(self):
        self.views_counter = self.views_counter + 1
        self.save()

    ## update views counter by 1 each time it's being requested
    def reset_views_counter(self):
        self.views_counter = 0
        self.save()

    ## show short version of a post
    def snippet(self):
        return self.content[:50] + '...'

    ## return it in a way you want it to be printed out   
    def __str__(self):
        return self.title

