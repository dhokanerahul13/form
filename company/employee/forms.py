from django import forms
from django import forms

class employeeregistration(forms.Form):
    name=forms.CharField(min_length=5,max_length=50,required=True)
    empid=forms.IntegerField(min_value=5,max_value=50)
    salary=forms.IntegerField(error_messages={'required':'enter your salary'})
    salarydate=forms.DateField()
    available = forms.BooleanField(widget = forms.Textarea)
    title = forms.CharField(widget = forms.Textarea)
    description = forms.CharField(widget = forms.CheckboxInput)
    views = forms.IntegerField(widget = forms.TextInput)
    agree=forms.BooleanField(label='i agree .......')