from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                              'placeholder': 'Введите фамилию'}))

    class Meta:

        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Ведите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                 'placeholder': 'Ведите пароль'}))

    class Meta:
        model = User
        fields = ('password', 'username')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                           'placeholder': 'Введите эл. почту'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                               'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                              'placeholder': 'Введите фамилию'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                  'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4',
                                                                  'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

