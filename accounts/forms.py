# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from .models import User


# 新的注册表单
class RegisterForm(UserCreationForm):
    # 保留邮箱字段，并将其设为必填
    email = forms.EmailField(required=True)

    # 隐藏角色字段，并将其默认值设置为 'student'
    role = forms.CharField(widget=forms.HiddenInput(), initial='student')

    class Meta(UserCreationForm.Meta):
        model = User
        # 简化字段，只保留用户名、邮箱和密码
        fields = ['username', 'email', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("该邮箱已被注册！")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


# 新的登录表单
class CustomAuthenticationForm(AuthenticationForm):
    # 修改标签，提示用户使用用户名或邮箱登录
    username = forms.CharField(label="用户名或邮箱")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = None
            # 1. 尝试使用用户名登录
            user = authenticate(self.request, username=username, password=password)

            if not user:
                # 2. 尝试使用邮箱登录
                try:
                    user = get_user_model().objects.get(email=username)
                    user = authenticate(self.request, username=user.username, password=password)
                except get_user_model().DoesNotExist:
                    pass

            if user:
                self.user_cache = user
            else:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
        return self.cleaned_data