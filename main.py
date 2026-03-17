from fastapi import FastAPI
from database import engine, Base

# Create tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Palé Builder Challenge API")

@app.get("/")
def root():
    return {"message": "Palé API is running"}