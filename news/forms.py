from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User


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
        title  = cleaned_data.get("title ")
        if title  is not None and len(title ) < 30:
            raise ValidationError({
                "text": "Текст не может быть менее 30 символов."
            })
        text = cleaned_data.get("text")
        if text == title:
            raise ValidationError(
                "Текст поста или новости не должен совпадать с заголовком."
            )
        return cleaned_data

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user