from fastapi import FastAPI, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routers import (guasave)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guasave.router)


if __name__ == "__main__":
    uvicorn.run(app)
