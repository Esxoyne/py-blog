from django import forms

from .models import Commentary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={"rows": 2})
        }
        labels = {
            "content": "",
        }