from fastapi import APIRouter, WebSocket

from app.websocket.connection_manager import manager

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def chat_socket(websocket: WebSocket, user_id: int):
    await manager.connect(websocket, user_id)
    print(manager.active_connections)

    try:
        while True:
            data = await websocket.receive_json()

            receiver_id = data["receiver_id"]
            message = data["message"]

            await manager.send_message(
                receiver_id,
                message
            )
    except:
        manager.disconnect(user_id)


