""" Schema for atm city data """

from django.db import models
from atm_management.models.atm_state import ATMState

class ATMCity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(ATMState, on_delete=models.RESTRICT)
   
    def __str__(self):
        return self.name