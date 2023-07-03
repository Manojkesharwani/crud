from django import forms
from .models import MYBLOGAPP


class mydata(forms.ModelForm):
    class Meta:
        model = MYBLOGAPP
        fields = ['name','lastname','Designation','create_date']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','style':'max-width:1300px','placeholder':'Enter Your Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','style':'max-width:1300px','placeholder':'Enter Your LastName'}),
            'Designation':forms.TextInput(attrs={'class':'form-control','style':'max-width:1300px','placeholder':'Enter Designation'}),
            'create_date':forms.TextInput(attrs={'class':'form-control','type':'date','style':'max-width:1300px','placeholder':'Enter Date'}),
        }