# socket_logic.py

import socketio

# Khởi tạo Socket.IO server
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=[])

# Sự kiện khi một client kết nối đến server
@sio.on('connect')
async def handle_connect(sid, environ, auth):
    print(f'Client connected: {sid}')

# Sự kiện khi một client tham gia vào phòng chat
@sio.on('join_room')
async def handle_join_room(sid, data):
    room_name = data.get('room_name')
    if room_name:
        sio.enter_room(sid, room_name)
        print(f'Client {sid} joined room {room_name}')

# Sự kiện khi một client gửi tin nhắn chat
@sio.on('chat_message')
async def handle_chat_message(sid, data):
    room_name = data.get('room_name')
    message = data.get('message')
    user_name = data.get('user_name')

    if room_name and message and user_name:
        # Phát tin nhắn đến tất cả client trong cùng phòng chat
        await sio.emit(
            'chat_message',
            {'user_name': user_name, 'message': message},
            room=room_name
        )
        print(f'Message from {user_name} in room {room_name}: {message}')

# Sự kiện khi một client ngắt kết nối
@sio.on('disconnect')
async def handle_disconnect(sid):
    print(f'Client disconnected: {sid}')