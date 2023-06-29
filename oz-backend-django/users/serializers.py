from rest_framework.serializers import ModelSerializer
from .models import User


class BoardUserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"

        fields = (
            "username",
            "gender",
            "age",
        )


# class AllUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

# 이걸 api에 담아서 가져온다.
