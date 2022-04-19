from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')



# u1 = Article.objects.get(pk=1)
# u1.articles.all() => u1 가 작성한 모든 articles
# u1.like_articles.all() => u1 이 좋아한 모든 글
# u1.followings.all() 