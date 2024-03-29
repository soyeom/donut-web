

from accountapp.views import User
from django.db import models
from accountapp.models import User
# Create your models here.

from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    content = models.TextField(null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='recomment')
    created_at = models.DateTimeField(auto_now=True)


