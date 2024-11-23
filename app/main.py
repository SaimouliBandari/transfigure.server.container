from fastapi import FastAPI
from .routers.excel import router
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=router, prefix='/excel', tags=['excel'])

if __name__ == "__main__":
    uvicorn.run(app=app,port=1503)