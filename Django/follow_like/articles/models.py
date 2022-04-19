from django.db import models
from django.conf import settings


class Article(models.Model):
    # 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')   
    # 좋아요 한 사용자
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')   # a.like_users.all() 
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}> {self.content}'
