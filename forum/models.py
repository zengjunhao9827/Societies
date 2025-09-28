from django.db import models
from accounts.models import User
from club.models import Club
from django.utils import timezone

# 模拟论坛帖子模型
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts', verbose_name="作者")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True, verbose_name="所属社团圈")
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    views = models.IntegerField(default=0, verbose_name="浏览量")
    likes = models.IntegerField(default=0, verbose_name="点赞数")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="发布时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "论坛帖子"
        verbose_name_plural = "论坛帖子"
        ordering = ['-created_at']
