from django import forms

from .models import CustomUser, Profile


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email",)

    def clean_password2(self):
        """
        Validate if the password match between password1 and password2.
        """
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords dont't match.")
        return cd["password2"]


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("user", "country")
