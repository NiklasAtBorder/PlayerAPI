from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List


class PlayerBase(SQLModel):
    name: str

class PlayerIn(PlayerBase):
    pass

class PlayerDb(PlayerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    events: List["EventDb"] = Relationship(back_populates="player")

class EventBase(SQLModel):
    type: str
    detail: str
    timestamp: datetime
    
class EventIn(EventBase):
    pass

class EventDb(EventBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    player_id: int = Field(foreign_key="playerdb.id")
    player: PlayerDb = Relationship(back_populates="events")
    


    

