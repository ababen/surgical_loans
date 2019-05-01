import datetime

from django.db import models

STATES = (
    ('NY', 'New York'),
    ('NJ', 'New Jersey'),
)

class Borrower(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    social_security = models.CharField(max_length=200, blank=True)
    address  = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=2, choices=STATES, default='NY', blank=True)
    zip = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)