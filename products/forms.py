from django import forms

from products.models import CommentModel, ColorsModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        exclude = ['created_at', 'product']
        model = CommentModel


