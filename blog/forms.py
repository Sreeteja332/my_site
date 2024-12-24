from django import forms

from .models import Comment

class ComentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude=['posts']
        labels={
            "user-name":"Your Name",
            "user-email":"Your Email",
            "text":"Your Comment"
        }