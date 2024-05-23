""" Schema for atm state data """

from django.db import models

class ATMState(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=2, blank=True, null=True) # NOTE: Here assumption is that country is always India otherwise a seperate model for country should be made

    def __str__(self):
        return self.name