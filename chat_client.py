import asyncio
import socketio
from concurrent.futures import ThreadPoolExecutor


sio = socketio.AsyncClient()
executor = ThreadPoolExecutor(max_workers=1)
USER_NAME = 'Simple Python Client'
ROOM_NAME = 'general'

# Hàm bất đồng bộ để nhận input từ bàn phím
async def get_input(prompt):
    return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)


@sio.event
async def connect():
    print(f'Connected as {USER_NAME} to server! ✅')
    await sio.emit('join_room', {'room_name': ROOM_NAME})


@sio.event
async def disconnect():
    print('Disconnected from server. ❌')


@sio.event
async def chat_message(data):
    print(f"\r[{data['user_name']}]: {data['message']}\n> ", end='', flush=True)


async def send_messages():
    await asyncio.sleep(2)  # Đợi 2 giây để đảm bảo đã join room

    while True:
        message = await get_input('>')
        if message.lower()  == 'quit':
            break
        await sio.emit('chat_message',
                       {'room_name':ROOM_NAME,'user_name': USER_NAME, 'message': message}
        )

    # ngắt kết nối
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