from django.shortcuts import render
from django.http import HttpResponseRedirect

from WebApp import forms

def EmpView(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print("Validations are Success Folks...!!")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            return HttpResponseRedirect('/Thanks')
    else:
        form = forms.EmpForm()
    return render(request, 'WebApp/FormPage.html', {'form': form})

def ThankView(request):
    return render(request, 'WebApp/Thanks.html')