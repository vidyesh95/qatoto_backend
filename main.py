from fastapi import FastAPI

app = FastAPI(title="Qatoto Backend API", description="API for Qatoto Frontend", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Qatoto Backend API"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}