from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):

    name = models.CharField("First name", max_length=25, blank=True)
    comment = models.TextField(blank=True, null=True)

