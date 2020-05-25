from django import forms
from .models import Teilnahme

CHOICES = (('OPTION_1', 'Holz'),
            ('OPTION_2', 'Öl/Kohle'),
            ('OPTION_3', 'Gas'),
            ('OPTION_4', 'Fernwärme'),
            ('OPTION_5', 'solar'),
            ('OPTION_6', 'Elektrisch'),

            )
CHOICES_1 = (('OPTION_1', 'EU strom-mix'),
            ('OPTION_2', 'Österreich strom-mix'),
            ('OPTION_3', 'Grünstrom'),
            ('OPTION_4', 'UZ 46 Ökostrom'),

            )

CHOICES_2 = (('OPTION_1', 'Nein'),
            ('OPTION_2', 'Ja'),
            )


CHOICES_3 = (('OPTION_1', 'Fast nie'),
            ('OPTION_2', 'Manchmal'),
            ('OPTION_3', 'Fast immer'),

            )

CHOICES_4 = (('OPTION_1', 'Nie'),
            ('OPTION_2', '1 Mal/Woche'),
            ('OPTION_3', '2 Mal/Woche'),
            ('OPTION_4', '3 Mal/Woche'),
            ('OPTION_5', '4 Mal/Woche'),
            ('OPTION_6', '5 Mal/Woche'),
            ('OPTION_7', '6 Mal/Woche'),
            ('OPTION_8', '7 Mal/Woche'),
            )


#modelForm
# class TeilnameForm(forms.Form):
#     vorname   = forms.CharField(widget=forms.TextInput(attrs={'class':'input1'}), max_length=100)
#     nachname  = forms.CharField(widget=forms.TextInput(attrs={'class':'input1'}), max_length=100)
#     email     = forms.EmailField(widget=forms.TextInput(attrs={'class':'input1'}))
#     alter     = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'input1'}))


class TeilnahmeForm(forms.ModelForm):

    vorname   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    nachname  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    email     = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    alter     = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Teilnahme
        fields = (

                'vorname',
                'nachname',
                'email',
                'alter',
                'ergebnis_1',
                'ergebnis_2',

                )



class FrageForm(forms.Form):
    frage    = forms.DecimalField(label="Wie groß ist Deine Wohnung/Dein Haus? (m2)",decimal_places=2,max_digits=5,initial=50,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_2  = forms.IntegerField(label="Wie viele Personen wohnen in der Wohnung/dem Haus?", initial=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_3  = forms.ChoiceField(label="Wie wird Deine Wohnung beheizt?",choices=CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_4  = forms.ChoiceField(label="Welche Art von Strom beziehst Du?", choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_5  = forms.IntegerField(label="Wie viele Haustiere beziehst Du (Hund oder Katze)?",initial=0,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_6  = forms.IntegerField(label="Wie viele km fährst Du pro Jahr mit dem Auto?",initial=10000,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_7  = forms.ChoiceField(label="Fährst Du voll elektrisch?", choices=CHOICES_2,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_8  = forms.DecimalField(label="Durchschnittsverbrauch des Fahrzeugs auf 100km?", decimal_places=2,max_digits=5,initial=5,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_9  = forms.DecimalField(label="Wie viele Stunden Flüge pro Jahr innerhalb Europa?", decimal_places=2,max_digits=5,initial=5,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_10 = forms.DecimalField(label="Wie viele Stunden Flüge pro Jahr außerhalb Europa?", decimal_places=2,max_digits=5,initial=1,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frage_11 = forms.ChoiceField(label="Kaufst Du Bio-Produkte?", choices=CHOICES_3,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_12 = forms.ChoiceField(label="Wie oft isst Du Milchprodukte oder Eier?",choices=CHOICES_4,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_13 = forms.ChoiceField(label="Wie oft isst Du Fleisch?", choices=CHOICES_4,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_14 = forms.ChoiceField(label="Achtest Du darauf, regionale und saisonale Lebensmittel zu kaufen?", choices=CHOICES_3,widget=forms.Select(attrs={'class': 'form-control'}))
    frage_15 = forms.ChoiceField(label="Achtest Du darauf, Lebensmittel nicht zu verschwenden?", choices=CHOICES_3,widget=forms.Select(attrs={'class': 'form-control'}))
