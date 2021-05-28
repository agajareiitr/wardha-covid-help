from django import forms
from django.forms import widgets
from .models import PlasmaDonar, PlasmaRequest,Groceries
from wardhacovidhelp import settings


class PlasmaRequestFormView(forms.ModelForm):
    DateOfPositive = forms.DateField(
        label="Date of Positive (dd/mm/yyyy)", input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = PlasmaRequest
        exclude = ['complete', "DateCreated", "verified"]
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Patient Full Name'}),
            'Age': forms.TextInput(attrs={'placeholder': 'Age'}),

        }


class PlasmaDonarFormView(forms.ModelForm):
    DateOfNegative = forms.DateField(
        label="Date of Recovery (dd/mm/yyyy)", input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = PlasmaDonar
        exclude = ['verified']
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Donar Full Name'}),
            'Age': forms.TextInput(attrs={'placeholder': 'Age'})
        }

class GroceriesFormView(forms.ModelForm):
    class Meta:
        model = Groceries
        exclude = ["Admin_Verified"]
        widgets = {
            'Store_Remarks':forms.Textarea(attrs={'placeholder':"Please Write few lines you want the customer to know about your Store like store open/close time,paid delivery charge,website link etc.",'rows':4, 'cols':5}),
            'Store_Name':forms.TextInput(attrs={'placeholder':"Store Full Name"}),
            "Address":forms.Textarea(attrs={"placeholder":"Store Full Address",'rows':4, 'cols':15}),
            "Phone_Number":forms.TextInput(attrs={"placeholder":"For Ex: 9876543210"})
        }