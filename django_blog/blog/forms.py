from django import forms
from .models import Comment
from taggit.forms import TagWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['content']
        widgets = {
            'tags': TagWidget(),  
        }
    def clean_content(self):  # Custom validation for the 'content' field
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) > 1000:
            raise forms.ValidationError("Comment is too long (max 1000 characters).")
        return content    