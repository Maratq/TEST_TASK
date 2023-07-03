from pydantic import BaseModel


class EntryCreate(BaseModel):
    uuid: str
    text: str
