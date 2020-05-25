from django import forms

class ContactForm(forms.Form):
    betreff = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Betreff','class':'form-control'}), max_length=100)
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    nachricht = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Nachricht','class':'form-control'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}), max_length=100)
