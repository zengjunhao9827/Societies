from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    # 学生主页 URL
    path('home/', views.student_home_view, name='home'),
    # 学生认证（占位）
    path('authenticate/', views.student_authenticate_view, name='authenticate'),
]
