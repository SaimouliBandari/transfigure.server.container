from fastapi import FastAPI
import uvicorn
import excel.controller as controller

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router=controller.router, prefix='/excel', tags=['excel'])

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)