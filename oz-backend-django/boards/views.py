# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Board
# from reviews.models import Review


# # Create your views here.
# def show_board(request):
#     return HttpResponse("show board123123123")


# def all_board(request):
#     # boards = Board.objects.all()

#     return HttpResponse("All board")


# # localhost:8000/board/1/asd
# def make_board(request, board_id, board_content):
#     return HttpResponse(f"Make board/ id: {board_id} / content: {board_content}")


# # Rendering
# def show_all_board(request):
#     boards = Board.objects.all()

#     return render(request, "all_boards.html", {"datas": boards, "status": "success"})


# # Rendering
# def show_board_reviews(request):
#     reviews = Review.objects.all()

#     return render(request, "reviews.html", {"datas": reviews, "status": "success"})


########################################################################################################################

# type() = QuerySet

# view.py
# 클라이언트에서 보낸 데이터를 받아서 처리해주는 부분
# HTTP METHOD
from rest_framework.views import APIView
from rest_framework.response import Response  # 클라이언트로 데이터를 내려주는 부분
from rest_framework.exceptions import NotFound  # 데이터를 찾지 못한 경우에 내려주는 오류
from .models import Board
from .serializers import BoardSerializer


# GET: 전체 게시글 불러오기
class Boards(APIView):
    def get(self, request):
        boards = Board.objects.all()  # board의 타입은 장고 객체; QuerySet

        # 장고 객체 -> JSON (Serializer); 바꿔줘야 한다.
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)


# URI = api/v1/board/1
# GET: 유저로부터 입력받은 id 값의 게시글 데이터 불러오기
class BoardDetail(APIView):
    def get(self, request, board_id):
        # request: React에서 데이터를 담아서 보내준 부분
        # board_id: URL을 통해서 데이터를 전달받는 부분
        try:
            board = Board.objects.get(id=board_id)  # 장고객체
        except Board.DoesNotExist:
            raise NotFound

        # 장고객체 -> JSON (Serializer)
        serializer = BoardSerializer(board)
        print(serializer)

        return Response(serializer.data)
