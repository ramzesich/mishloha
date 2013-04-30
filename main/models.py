from django.conf import settings
from django.db import models


class Customer(models.Model):
    id           = models.AutoField(primary_key=True)
    f_name       = models.CharField(max_length=50, default=None)
    l_name       = models.CharField(max_length=50, default=None)
    company_name = models.CharField(max_length=200, default=None)
    email        = models.CharField(max_length=50, default=None)
    phone        = models.CharField(max_length=25, default=None)
    
    def __str__(self):
        return "{0} {1}".format(self.f_name, self.l_name)
    
    class Meta:
        ordering = ['id']
        db_table = 'customers'