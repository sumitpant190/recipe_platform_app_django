from django import forms
from .models import Recipe, Rating, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'category','image']
        widgets = {
            'category': forms.Select()
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3})
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError('Rating must be between 0 and 5.')
        return rating
