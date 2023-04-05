from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Comment


# Форма регистрации.
class SigUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
        'id': "inputUsername",
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'id': "inputPassword",
    }))
    repeat_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'id': "ReInputPassword",
    }))

    # Метод для валидации форм.
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        # Если пароли не совпадают.
        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

    # Метод для сохранения данных формы в базу данных.
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


# Форма авторизации.
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': "form-control",
        'id': "inputUsername",
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': "form-control mt-2",
        'id': "inputPassword",
    }))


# Форма обратной связи.
class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': "Ваше имя"
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': "Ваша почта"
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'placeholder': "Тема"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control md-textarea',
        'id': 'message',
        'rows': 2,
        'placeholder': "Ваше сообщение"
    }))


# Форма комментарии.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
