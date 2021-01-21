from django import forms

from comment.models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['nickname', 'email', 'text']
