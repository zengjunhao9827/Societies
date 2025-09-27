from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    自定义用户模型
    """
    ROLE_CHOICES = (
        ('student', '普通学生'),
        ('member', '社团成员'),
        ('vice_leader', '社团副会长'),
        ('leader', '社团会长'),
        ('admin', '后台管理员'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # 新增字段：用于学生认证（模拟学号认证）
    is_verified = models.BooleanField(default=False, verbose_name="是否已认证")

    # 新增字段：用于模拟当前用户的社团信息
    club_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="所属社团")

    def is_student(self):
        return self.role == 'student'

    def is_member(self):
        return self.role in ['member', 'vice_leader', 'leader']

    def is_vice_leader(self):
        return self.role == 'vice_leader'

    def is_leader(self):
        return self.role == 'leader'

    def is_admin(self):
        return self.role == 'admin'

    # 判断是否已加入社团
    def has_club(self):
        return bool(self.club_name)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
