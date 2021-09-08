from django import forms
from admission.models import Student
#from django.forms import fields, models
#from admission.models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = '__all__'