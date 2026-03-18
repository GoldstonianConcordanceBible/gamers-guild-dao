from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gamers Guild DAO API LIVE"}

@app.get("/health")
def health():
    return {"status": "healthy"}