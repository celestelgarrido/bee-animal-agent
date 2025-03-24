from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    name: str
    owner: str
