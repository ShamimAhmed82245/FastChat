from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from app.api.routes import auth
from app.db.database import Base, engine
from app.websocket.chat import router as ws_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ws_router)
@app.get("/", response_class=HTMLResponse)
def home():
    data = """
     <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Web Page</title>
</head>
<body>

    <h1>Welcome to My Website</h1>
    <p>This is a paragraph of text on a basic HTML page.</p>
    
    <!-- This is a comment. It won't show up on the webpage. -->
    <a href="https://wikipedia.org">Visit Wikipedia</a>

    <input id ="message" type = "text" placeholder="Enter your name">
    <button onclick = "sendMessage()">Submit</button>

    <ul id = "messageList"></ul>

    <script>
        const ws = new WebSocket("ws://127.0.0.1:8000/socket");

        ws.onopen = () => {
            console.log("connected__onopen");
        }

        ws.onconnect = () =>{
            console.log("connected");
        }

        ws.onmessage = (event) => {
            console.log("Message from server ", event.data);
            const messageList = document.getElementById("messageList");
            const newMessage = document.createElement("li");
            newMessage.textContent = event.data;
            messageList.appendChild(newMessage);    
            
        }

        ws.onerror = (error) =>{
            console.log(error);
        }
        
        function sendMessage(){
            const messageInput = document.getElementById("message");
            const message =  messageInput.value;
            ws.send(message);
        }
    </script>

</body>

</html>

    """
    return data
    # return {"message": "FastAPI JWT Auth Running"}

@app.websocket("/socket")
async def websocket_test(websocket:WebSocket):
    
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Server received: {data}")
