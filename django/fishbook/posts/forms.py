from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['species', 'description']
    labels = {
      'species': '어종',
      'description': '설명',
    }
    widget = {
      'species': forms.TextInput(attrs={
        'class': 'form-control'
      }),
      'description': forms.Textarea(attrs={
        'class': 'form-control'
      }),
    }
