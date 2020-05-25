from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Your email','class': 'form-control'}))
    class Meta:
        model = Join
        fields = ['email']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        print('meine email:'+str(email))
        qs = Join.objects.filter(email=email)
        print('mein obj:'+str(qs))
        if qs.exists():
            print(' i bin au sogar dooooooo')
            raise forms.ValidationError("This eamil already exists")
        else:
            return
