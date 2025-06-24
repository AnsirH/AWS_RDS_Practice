from django.urls import path
from .views import board_lists, board_new, board_update, board_delete

urlpatterns = [
    path('new/', board_new, name="board_new"), # create
    path('', board_lists, name="board_lists"), # read
    path('update/<int:pk>', board_update, name="board_update"), # update
    path('delete<int:pk>', board_delete, name="board_delete"), # delete
]