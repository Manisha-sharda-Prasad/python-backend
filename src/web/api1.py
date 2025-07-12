from fastapi import FastAPI
app = FastAPI()

@app.get("/hw")
def read_root():
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    return {"message": "Welcome to FastAPI!"}

