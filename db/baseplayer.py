from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class PlayerBase(SQLModel):
    name: str

class PlayerIn(PlayerBase):
    pass

class PlayerDb(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)

    events: list["EventDb"] = Relationship(back_populates="player")

class EventBase(SQLModel):
    type: str
    detail: str
    timestamp: datetime
    
class EventIn(EventBase):
    pass

class EventDb(EventBase, table=True):
    player_id: int = Field(foreign_key="playerdb.id")
    id: int = Field(default=None, primary_key=True)

    player: PlayerDb = Relationship(back_populates="events")
    
    
    


    

