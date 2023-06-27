from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 아이디, 패스워드, 닉네임, 이메일,폰넘버, 게시판이름
class User(AbstractUser):
    first_name = models.CharField(("first name"), max_length=150, blank=False)
    last_name = models.CharField(("last name"), max_length=150, blank=False)

    name = models.CharField(max_length=30)
    description = models.TextField()

    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10)

    is_business = models.BooleanField(default=False)  # is it business account?

    def __str__(self):
        return f"{self.name} / {self.age} / {self.description}"  # 관리자 페이지에서 내가 원하는 데이터만 볼 수 있다.

    # password =
    # nickname =
    # email =
    # phone_number =
    # board_name =


# 좋아요갯수, 댓글갯수, 날짜, 내용, 작성자, 사진, 위치, 이미지
# class Board(models.Model):
#     like_num = models.PositiveIntegerField()
#     review_num = models.PositiveIntegerField()

#     writer_date = models.CharField(max_length=50)

#     writer = models.CharField(max_length=50)
#     content = models.TextField()
