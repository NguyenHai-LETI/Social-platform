# chat_client.py

import asyncio
import socketio

sio = socketio.AsyncClient()

USER_NAME = 'Simple Python Client'
ROOM_NAME = 'general'


@sio.event
async def connect():
    print(f'Connected as {USER_NAME} to server! ✅')
    await sio.emit('join_room', {'room_name': ROOM_NAME})


@sio.event
async def disconnect():
    print('Disconnected from server. ❌')


@sio.event
async def chat_message(data):
    print(f"[{data['user_name']}]: {data['message']}")


async def send_messages():
    await asyncio.sleep(2)  # Đợi 2 giây để đảm bảo đã join room

    messages = [
        "Xin chào mọi người!",
        "Đây là một tin nhắn tự động từ client Python.",
    ]

    for msg in messages:
        await sio.emit(
            'chat_message',
            {'room_name': ROOM_NAME, 'user_name': USER_NAME, 'message': msg}
        )
        print(f'Sent: {msg}')
        await asyncio.sleep(1)

    # Cho phép client tồn tại trong 5 giây rồi ngắt kết nối
    print("Sending finished, staying online for 5 more seconds...")
    await asyncio.sleep(5)
    print("Exiting...")
    await sio.disconnect()


async def main():
    try:
        await sio.connect('http://localhost:8000')
        await send_messages()
        await sio.wait()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    asyncio.run(main())