from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'published_date', 'status', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input form-control'}),
            'slug': forms.TextInput(attrs={'class': 'input form-control'}),
            'author': forms.Select(attrs={'class': 'input form-control'}),
            'content': forms.Textarea(attrs={'class': 'input textarea form-control'}),
            'published_date': forms.DateTimeInput(attrs={'class': 'input form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'input form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'input form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input form-control'}),
            'slug': forms.TextInput(attrs={'class': 'input form-control'}),
        }