from fastapi import FastAPI
from animal.src.api.simpleAgent import agent

app = FastAPI(title="Mi API con FastAPI")

# Include routers endpoints
app.include_router(agent)

 