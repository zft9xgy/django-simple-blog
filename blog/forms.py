from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'published_date', 'status', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input form-control h-full-width'}),
            'slug': forms.TextInput(attrs={'class': 'input form-control h-full-width'}),
            'content': forms.Textarea(attrs={'class': 'input textarea form-control h-full-width'}),
            'published_date': forms.DateTimeInput(attrs={'class': 'input form-control h-full-width', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'input form-control h-full-width'}),
            'tags': forms.SelectMultiple(attrs={'class': 'input form-control h-full-width'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input form-control h-full-width'}),
            'slug': forms.TextInput(attrs={'class': 'input form-control h-full-width'}),
        }


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input h-full-width'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['role', 'user'] 

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input h-full-width'})