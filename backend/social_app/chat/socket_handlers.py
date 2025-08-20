import socketio

class ChatNamespace(socketio.AsyncNamespace):
    def on_join_room(self, sid, data):
        room_name = data.get('room_name')
        if room_name:
            self.enter_room(sid, room_name)
            print(f'Client {sid} joined room {room_name}')

    async def on_chat_message(self, sid, data):
        room_name = data.get('room_name')
        message = data.get('message')
        user_name = data.get('user_name')

        if room_name and message and user_name:
            await self.emit(
                'chat_message',
                {'user_name': user_name, 'message': message},
                room=room_name
            )
            print(f'Message from {user_name} in room {room_name}: {message}')

    def on_connect(self, sid, environ):
        # Bạn có thể xử lý sự kiện kết nối tại đây nếu nó chỉ liên quan đến chat
        pass