import socketio
from django.conf import settings
from chat.socket_handlers import ChatNamespace

#lấy cấu hình CORS trong setting cho socket server
allowed_origins = settings.CORS_ALLOWED_ORIGINS
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=allowed_origins)

# Đăng ký namespace
sio.register_namespace(ChatNamespace('/chat'))

# Sự kiện chung client kết nối đến server
@sio.on('connect')
async def handle_connect(sid, environ, auth):
    print(f'Client connected: {sid}')

# Sự kiện chung  client ngắt kết nối
@sio.on('disconnect')
async def handle_disconnect(sid):
    print(f'Client disconnected: {sid}')


