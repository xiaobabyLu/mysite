from django.forms import ModelForm
from polls.models import Question
from django import forms


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(),max_length=100)
    email = forms.CharField(label='电子邮件')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())