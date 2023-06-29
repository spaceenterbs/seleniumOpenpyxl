# from rest_framework.serializers import ModelSerializer
# from .models import Board


# class BoardSerializer(ModelSerializer):
#     class Meta:
#         model = Board
#         fields = "__all__"


from rest_framework.serializers import ModelSerializer
from .models import Board
from users.models import User

from users.serializers import BoardUserSerializer
from reviews.serializers import ReviewSerializer


# (1) 전체 데이터를 다 보여주는 Serialize
class BoardSerializer(ModelSerializer):
    user = BoardUserSerializer()
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = "__all__"
        # depth = 1 # foreign key에 해당 정보를 내리고 내리고


#             # 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻
#             # Board - User 모델 => 현재 코드는 Board 모델 객체를 직렬화 하고 있지만,
#             # depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
#             depth = 1 # objects도 serialize화 시킴


# # (2) 일부 데이터만 보여주는 Serialize
# class BoardListSerializer(ModelSerializer):
#     class Meta:
#         model = Board
#         fields = ("id", "content", "like")
