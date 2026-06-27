from fastapi import FastAPI
from app.api.routes import auth
from app.db.database import Base, engine
from app.websocket.chat import router as ws_router
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ws_router)
@app.get("/")
def home():
    return {"message": "FastAPI JWT Auth Running"}