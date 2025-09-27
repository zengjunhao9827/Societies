from django.db import models
from accounts.models import User
from django.utils import timezone

# 模拟社团模型
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="社团名称")
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='led_clubs', verbose_name="社长")
    description = models.TextField(verbose_name="社团简介")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "社团"
        verbose_name_plural = "社团"

# 模拟社团活动模型
class Activity(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='activities', verbose_name="所属社团")
    title = models.CharField(max_length=200, verbose_name="活动标题")
    date = models.DateField(verbose_name="活动日期")
    location = models.CharField(max_length=100, verbose_name="活动地点")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")

    def __str__(self):
        return f"{self.title} ({self.club.name})"

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = "活动"
        ordering = ['-date']
