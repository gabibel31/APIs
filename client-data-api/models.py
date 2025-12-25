from pydantic import BaseModel, EmailStr
from typing import List, Optional
class Client(BaseModel):
    id: int
    name: str
    email: Optional[EmailStr]
class ClientRequest(BaseModel):
    clients : List[Client]