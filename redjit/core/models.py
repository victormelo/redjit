from django.db import models
from vote.managers import VotableManager
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    votes = VotableManager()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    link = models.ForeignKey(Link)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s on %s' % (self.user, self.link.id)
