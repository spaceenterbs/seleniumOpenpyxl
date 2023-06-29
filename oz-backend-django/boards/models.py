from django.db import models
from common.models import CommonModel


# 좋아요갯수, 댓글갯수, 날짜, 내용, 작성자, 사진, 위치, 이미지
class Board(CommonModel):
    like_num = models.PositiveIntegerField()
    review_num = models.PositiveBigIntegerField()

    write_date = models.CharField(max_length=50)

    writer = models.CharField(max_length=50)
    content = models.TextField()

    # user 데이터가 지워지면 게시글도 지워주세요.
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # # user 데이터가 지워져도 게시글은 남겨주세요.
    # user = models.ForeignKey("users.User", on_delete=models.SET_NULL)
