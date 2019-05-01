import datetime

from django.db import models

class Loans(models.Model):
    loan_name = models.CharField(max_length=200)
    loan_date = models.DateField(auto_now_add=True)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    compount_method = models.CharField(max_length=200)
    application_fee = models.DecimalField(max_digits=6, decimal_places=2)
    case_fee = models.DecimalField(max_digits=6, decimal_places=2)
    incident_date = models.DateField()

    def recent_loans(self):
        return self.loan_name >= datetime.now() - datetime.timedelta(days=1)

    def __str__(self):
        return '%s %s' % (self.loan_name, self.loan_date)
