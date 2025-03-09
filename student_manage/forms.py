from django import forms
from .models import Student

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=Student
        fields ="__all__"
        labels ={
            "fname":"FirstName",
            "lname":"LastName",
            "email":"Email Id",
            "phone":"phone no",
            "branch":"Branch"
        }
    widgets ={
        "fname":forms.TextInput(attrs={"class":"form-control"}),
        "lname":forms.TextInput(attrs={"class":"form-control"}),
        "fname":forms.TextInput(attrs={"class":"form-control"}),
        "phone":forms.NumberInput(attrs={"class":"form-control"}),
        "branch":forms.Select(attrs={"class":"form-control"}),
    }
