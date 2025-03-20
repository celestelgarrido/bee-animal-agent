from fastapi import FastAPI
from animal.src.api.user import user

app = FastAPI(title="Mi API con FastAPI")

# Incluir los routers de los endpoints
app.include_router(user)

@app.get("/")
def root():
    return {"message": "Bienvenido a mi API"}
