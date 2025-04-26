from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..db.baseplayer import PlayerIn, PlayerDb, EventIn
from ..db.database import get_session
from ..db import crud



router = APIRouter()

@router.post("/players", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return crud.create_player(session, player_in)

@router.get("/players", response_model=list[PlayerDb])
def get_player(name: str = "", session: Session = Depends(get_session)):
    return crud.get_player(session, name)

@router.get("/players/{player_id}", response_model=PlayerDb)
def get_player_by_id(player_id: int, session: Session = Depends(get_session)):
    return crud.get_player_by_id(session, player_id)

@router.delete("/players/{player_id}")
def delete_player(player_id: int, session: Session = Depends(get_session)):
    return crud.delete_player(session, player_id)

@router.post("/players/{player_id}/events", status_code=status.HTTP_201_CREATED)
def create_event(player_id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return crud.create_event(session, player_id, event_in)

@router.get("/players/{player_id}/events", response_model=list[EventIn])
def get_events(player_id: int, session: Session = Depends(get_session)):
    return crud.get_events(session, player_id)
