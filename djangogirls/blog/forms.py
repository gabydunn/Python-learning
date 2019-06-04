from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        #model to be reflected in form
        model = Post
        #fields to end up on form 
        fields = ('title', 'text',)