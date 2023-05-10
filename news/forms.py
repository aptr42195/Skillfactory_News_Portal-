from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'author',
           'post_category'
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       if text is not None and len(text) < 30:
           raise ValidationError({
               "text": "Текст не может быть менее 30 символов."
           })
       title = cleaned_data.get("title")
       if title == text:
           raise ValidationError(
               "Текст не должен быть идентичен названию."
           )
       return cleaned_data