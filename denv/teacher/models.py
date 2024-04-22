from django.db import models

# Create your models here.
class Blood_group(models.Model) :
   blood_group = models.CharField(max_length=3)

   def __str__(self):
       return self.blood_group

   class Meta :
      ordering = ['blood_group']
   