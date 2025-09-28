from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from club.models import Activity, Club
from forum.models import Post
from accounts.models import User  # 导入User模型


@login_required
def student_home_view(request):
    """学生主页视图：展示活动、帖子和个人信息"""

    # 1. 获取核心数据
    # 热门活动：按 is_hot 排序或按日期排序
    hot_activities = Activity.objects.all().order_by('-is_hot', '-date')[:5]

    # 热门帖子：按点赞数和浏览量排序
    hot_posts = Post.objects.all().order_by('-likes', '-views')[:5]

    # 所有社团列表（用于交流圈和申请）
    all_clubs = Club.objects.all()[:8]

    # 2. 模拟 AI 助手入口
    ai_assistant_url = "#"  # 实际应指向 ai:assistant 视图

    context = {
        'hot_activities': hot_activities,
        'hot_posts': hot_posts,
        'all_clubs': all_clubs,
        'ai_assistant_url': ai_assistant_url,
    }
    return render(request, 'student/home.html', context)


@login_required
def student_authenticate_view(request):
    """
    学生认证视图（占位）：
    实际场景中，这里应该包含学号、姓名输入和后端校验逻辑。
    认证成功后更新 request.user.is_verified = True
    """
    if request.method == 'POST':
        # 模拟认证成功，实际请替换为你的认证逻辑
        request.user.is_verified = True
        # 模拟设置学号（如果注册时没有的话）
        # request.user.student_id = "12345678"
        request.user.save()
        return redirect('student:home')

    # 简单的认证表单页面
    return render(request, 'student/authenticate.html')
