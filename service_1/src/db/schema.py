from pydantic import BaseModel 


class MusicRequest(BaseModel):
    id: int
    email: str
    state: str
    songid: str