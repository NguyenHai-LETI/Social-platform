import os
import socketio
from django.core.asgi import get_asgi_application

#set env environment for django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_app.settings.develop')

#Init ASGI Application for HTTP
django_asgi_app = get_asgi_application()

from .socket_logic import sio

"""Kết hợp ứng dụng Socket.IO và Django
Mọi yêu cầu đến đường dẫn '/socket.io/' sẽ được xử lý bởi sio.
Các yêu cầu khác sẽ được chuyển cho Django."""
application = socketio.ASGIApp(sio, other_asgi_app=django_asgi_app)