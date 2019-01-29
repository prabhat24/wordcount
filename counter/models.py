from django.db import models
class cont(models.Model):
    name=models.CharField(max_length=30)
    contact_det=models.CharField(max_length=10)
    #def __str__(self):
    #    lt=[self.name,self.contact_det]
    #    return lt



