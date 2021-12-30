from django import forms

class registerform(forms.Form):
    username= forms.CharField()
    password= forms.CharField()
    repassword=forms.CharField()
    email=forms.EmailField()
    phone=forms.IntegerField()
    dob=forms.DateField()
    li=[['MALE','Male'],['FEMALE','Female']]
    gender=forms.ChoiceField(choices=li)