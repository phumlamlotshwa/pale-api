from fastapi import FastAPI
from database import engine, Base
from routes import users, protected

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Palé Builder Challenge API")

app.include_router(users.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected.router, prefix="/user", tags=["Protected"])

@app.get("/")
def root():
    return {"message": "Palé API is running"}