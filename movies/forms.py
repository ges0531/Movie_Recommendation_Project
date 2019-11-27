from .models import Movie, Genre, Review
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class MovieModelForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    overview = forms.Textarea()
    popularity = forms.IntegerField()
    poster_url = forms.CharField(max_length=100)
    runtime = forms.IntegerField()

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'popularity', 'poster_url', 'runtime')
        widget = {
            'overview': forms.Textarea(attrs={
                'col': 80,
                'row': 20,
            })
        }

class GenreModelForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Genre
        fields = ('name', )


class ReviewModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=100)
    rate = forms.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    class Meta:
        model = Review
        fields = ('content', 'rate', )


