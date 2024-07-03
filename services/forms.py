from django import forms
from services.models import Travel , Annonce

typevoyage = (
    ('Aller simple','Aller Simple'),
    ('Aller retour','Aller-Retour')
)

class TravelForm(forms.ModelForm):
    type = forms.ChoiceField(choices=typevoyage , widget=forms.Select(
        attrs={
            'class':'form-control',
            'id' : 'type',
            'name':'type'
        }
    ))
    
    file = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class':'form-control mt-3',
                'id':'id_image',
                'name':'image',
                'type':'file',
                
            }
        )
    )
    
    airline = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nom de la compagnie',
                'id' : 'airline',
                'name':'airline'
                
            }
        )
    )
    flight_number = forms.CharField(
         widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Numero de vol',
                'id' : 'flight',
                'name':'flight'
                
            }
        )
    )
    origin =forms.CharField( widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Lieu de depart',
                'id' : 'origin',
                'name':'origin'
                
            }
        ))
    destination = forms.CharField( widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Lieu de destination',
                'id' : 'destination',
                'name':'destination'
                
            }
        ))
    departure_date = forms.DateTimeField(
         widget=forms.DateTimeInput(
            attrs={
                'type':'datetime-local',
                'class':'form-control',
                'id' : 'departure_date',
                'name':'departure_date'
                
            }
        )
    )
    arrival_date = forms.DateTimeField(
          widget=forms.DateTimeInput(
            attrs={
                'type':'datetime-local',
                'class':'form-control',
                'id' : 'arrival_date',
                'name':'arrival_date'
                
            }
        )
    )
    
    class Meta:
        model = Travel
        fields = ['type','file','airline','flight_number','origin','destination','departure_date','arrival_date']
    
    
    
class AnnonceForm(forms.ModelForm):
    title = forms.CharField(
        label="Nom de l'annonce",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                "id": "title",
                "name":"title",
                'placeholder':"Nom de l'annonce"
            }
        )
    )
    description = forms.CharField(
        label="Description de l'annonce",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'id':"description",
                'name':"description",
                'placeholder':"Description de l'annonce"
            }
        )
    )
    capacity = forms.IntegerField(
        label="Quantité à vendre",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':"Quantité à vendre",
                'id':"capacity",
                'name':"capacity"
            }
        )
    )
    price = forms.FloatField(
        label="Prix par kilo",
        widget=forms.NumberInput(
            
            attrs={
                'class':'form-control',
                'id':'price',
                'name':"price",
                'placeholder':"Prix par kilo"
            }
        )
    )
    class Meta:
        model = Annonce
        fields = ['title','description','capacity','price']
    