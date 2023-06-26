from django.db import models


# Create your models here.
# 댓글저자, 작성날짜, 내용, 그림내용
class Review(models.Model):
    review_writer = models.CharField(max_length=50)

    review_writer_date = models.CharField(max_length=50)

    content = models.TextField
    content_image = models.ImageField()  # 댓글에 이미지 넣기


# 좋아요갯수, 댓글갯수, 날짜, 내용, 작성자, 사진, 위치, 이미지
# class Board(models.Model):
#     like_num = models.PositiveIntegerField()
#     review_num = models.PositiveIntegerField()
#     writer_date = models.CharField(max_length=50)
#     writer = models.CharField(max_length=50)
#     content = models.TextField()
