from django import forms
from django.contrib.auth.models import User
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name',
                  'text_comments', 'email')



class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput,
    )

    password2 = forms.CharField(
        label="repeat password",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords are not equal")
        return cd["password2"]