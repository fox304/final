from django import forms
from django.contrib.auth import get_user_model

from myrecipes.models import Recipe


class Users(forms.Form):
    user_name = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class RegistrationUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Делаем обязательным поле first_name('имя') """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True

    username = forms.CharField(label="ваш логин")
    password = forms.CharField(label="пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password', 'password2', 'email']
        labels = {
            'first_name': 'Ваше имя',
            'last_name': 'фамилия',
        }

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("пароли должны совпадать")
        if len(self.cleaned_data['password']) < 6:
            raise forms.ValidationError('количество символов должно быть не менее 6')
        return self.cleaned_data['password']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe

        fields = ('name', 'ingredients', 'description',
                  'steps', 'time_minutes', 'image', 'category', 'author')

        exclude = ('author',)
