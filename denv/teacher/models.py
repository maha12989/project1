from django.db import models

# Create your models here.
class Blood_group(models.Model) :
   blood_group = models.CharField(max_length=3)

   def __str__(self):
       return self.blood_group

   class Meta :
      ordering = ['blood_group']
    
    
      
class Info(models.Model) :
   name = models.CharField(max_length=30)
   age = models.PositiveIntegerField()
   salary = models.PositiveIntegerField()
   blood_group = models.ForeignKey(Blood_group, on_delete=models.CASCADE, default=1)

   def __str__(self):
       return self.name

   class Meta :
      ordering = ['-salary']
      

   