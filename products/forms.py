from django import forms
class searchForm(forms.Form):
    search_name=forms.CharField(max_length=200)
class cartForm(forms.Form):
    name=forms.CharField(max_length=200)

class removeForm(forms.Form):
    name=forms.CharField()
class checkForm(forms.Form):
    name=forms.CharField(max_length=100)
    phone_number=forms.IntegerField()
    address=forms.CharField(max_length=100)
    mail=forms.EmailField()
    