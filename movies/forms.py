from .models import Movie, Genre, Review, Date
from django import forms

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
    content = forms.CharField(max_length=100)
    rate = forms.IntegerField()

    class Meta:
        model = Review
        fields = ('content', 'rate', )

class DateModelForm(forms.ModelForm):
    release_date = forms.DateTimeField()

    class Meta:
        model = Date
        fields = ('release_date', )