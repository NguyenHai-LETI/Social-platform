from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny


@AllowAny
def chat_room(request, room_name):
    # Bạn có thể thêm logic để kiểm tra quyền truy cập phòng chat tại đây
    return render(request, 'chat/chat_room.html', {'room_name': room_name})