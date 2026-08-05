from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database.db import Base, engine

# Import model agar tabel otomatis dibuat
from models.memory import Memory
from models.profile import Profile

# Router
from routes.chat import router as chat_router

# Memory Manager
from memory.memory_manager import (
    lihat_memory,
    hapus_profile,
    hapus_chat
)

# ==========================
# DATABASE
# ==========================

Base.metadata.create_all(bind=engine)

# ==========================
# FASTAPI
# ==========================

app = FastAPI(
    title="CenAI",
    version="1.0.0"
)

# ==========================
# CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# STATIC
# ==========================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# ==========================
# TEMPLATE
# ==========================

templates = Jinja2Templates(
    directory="templates"
)

# ==========================
# ROUTER
# ==========================

app.include_router(chat_router)

# ==========================
# HOME
# ==========================

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "CenAI"
        }
    )

# ==========================
# MEMORY API
# ==========================

@app.get("/memory/{user_id}")
def get_memory(user_id: str):
    return lihat_memory(user_id)


@app.delete("/memory/profile/{user_id}")
def delete_profile(user_id: str):

    hapus_profile(user_id)

    return {
        "success": True,
        "message": "Profile berhasil dihapus."
    }


@app.delete("/memory/chat/{user_id}")
def delete_chat(user_id: str):

    hapus_chat(user_id)

    return {
        "success": True,
        "message": "Riwayat chat berhasil dihapus."
    }


@app.delete("/memory/all/{user_id}")
def delete_all(user_id: str):

    hapus_profile(user_id)
    hapus_chat(user_id)

    return {
        "success": True,
        "message": "Semua memory berhasil dihapus."
    }