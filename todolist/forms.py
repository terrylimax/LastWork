from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=200, label='Имя')
    last_name = forms.CharField(max_length=200, label='Фамилия')
    username = forms.CharField(max_length=200, label='Логин')
    password = forms.CharField(max_length=200, label='Пароль')
    email = forms.CharField(max_length=200, label='Email')