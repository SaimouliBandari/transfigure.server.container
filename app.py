from fastapi import FastAPI
from src.routers.excel import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=router, prefix='/excel', tags=['excel'])

if __name__ == "__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=1503)