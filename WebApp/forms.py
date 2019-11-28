from django import forms

class EmpForm(forms.Form):
    Name = forms.CharField()
    Salary = forms.IntegerField()