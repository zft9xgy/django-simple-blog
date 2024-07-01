from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})