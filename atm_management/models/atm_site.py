""" Schema for atm site data """

from django.db import models
from atm_management.models.atm_city import ATMCity
from atm_management.models.atm_state import ATMState

class ATMSite(models.Model):

    name = models.CharField(max_length=255)
    site_id = models.IntegerField(unique=True) 
    contact_details = models.JSONField(null=True, blank=True)

    address_line_1 = models.TextField(null=True, blank=True)
    address_line_2 = models.TextField(null=True, blank=True)
    city = models.ForeignKey(ATMCity, on_delete=models.RESTRICT)
    pincode = models.IntegerField()
    
    updated_at     =  models.DateTimeField(auto_now=True)
    created_at     =  models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return f"{self.site_id} ({self.name})"

    