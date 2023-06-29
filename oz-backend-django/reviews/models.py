from django.db import models
from common.models import CommonModel


# 작성자, 날짜, 좋아요 수, 내용
class Review(models.Model):
    like_num = models.PositiveIntegerField()
    content = models.TextField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
