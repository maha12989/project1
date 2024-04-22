from django import forms
from .models import Blood_group, Info
class InfoForm(forms.ModelForm) :
   class Meta :
      model = Info
      fields = ['name', 'age', 'salary', 'blood_group']

class BloodForm(forms.ModelForm) :
   class Meta :
      model = Blood_group
      fields = ['blood_group']