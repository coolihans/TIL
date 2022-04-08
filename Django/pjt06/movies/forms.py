from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    GENRE_A = 'comedy'
    GENRE_B = 'horror'
    GENRE_C = 'romance'
    GENRES_CHOICES = [
        (GENRE_A, '코미디'),
        (GENRE_B, '호러'),
        (GENRE_C, '로맨스'),
    ]

    genre = forms.ChoiceField(choices=GENRES_CHOICES, widget=forms.Select())
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max':5
            }
        )
    )
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        
    )

    class Meta:
        model = Movie
        fields = '__all__'
