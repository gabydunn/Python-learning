from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        #model to be relected in form
        model = Post
        #fields to end up on form 
        fields = ('title', 'text',)