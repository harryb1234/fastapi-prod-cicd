from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI CI/CD App Running Succesfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}
