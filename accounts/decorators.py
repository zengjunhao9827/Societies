from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles=[]):
    """
    只允许特定角色访问
    用法：
    @role_required(['leader', 'admin'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            if request.user.role not in allowed_roles:
                return redirect('accounts:unauthorized')  # 可自定义提示页面
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
