from django import forms
from .models import *

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check= forms.BooleanField(label="Completed", required=False)
    file=forms.FileField()
class UserForm(ModelForm):
    class Meta:
       model=ToDoList
       fields='__all__'
       
    
    
    
