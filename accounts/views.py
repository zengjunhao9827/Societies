# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, CustomAuthenticationForm # 导入我们自定义的表单
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# 注册视图
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 注册后自动登录
            messages.success(request, f"注册成功！欢迎来到智慧校园社团论坛，{user.username}！")
            return redirect_home_by_role(user)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"欢迎回来，{user.username}！")
            return redirect_home_by_role(user)
        else:
            # 登录失败，显示更友好的错误信息
            messages.error(request, "用户名、邮箱或密码错误，请重试。")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
# 登出视图
@login_required # 确保只有已登录用户才能访问
def logout_view(request):
    logout(request)
    messages.info(request, "您已成功登出。")
    return redirect('accounts:login')

def redirect_home_by_role(user):
    """根据角色跳转到不同主页"""
    if user.is_student():
        return redirect('student:home')
    elif user.is_member() or user.is_vice_leader() or user.is_leader():
        return redirect('club:home')
    elif user.is_admin():
        return redirect('adminsys:dashboard')
    else:
        return redirect('student:home')

# 未授权页面
def unauthorized_view(request):
    return render(request, 'accounts/unauthorized.html', {'message': '您没有权限访问该页面'})