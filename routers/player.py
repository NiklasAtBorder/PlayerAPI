from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..db.baseplayer import PlayerIn, PlayerDb, EventIn
from ..db.database import get_session
from ..db import player_crud, event_crud


router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return player_crud.create_player(session, player_in)

@router.get("/", response_model=list[PlayerDb])
def get_player(name: str = "", session: Session = Depends(get_session)):
    return player_crud.get_player(session, name)

@router.get("/{id}", response_model=PlayerDb)
def get_player_by_id(player_id: int, session: Session = Depends(get_session)):
    return player_crud.get_player_by_id(session, player_id)

@router.post("/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event(player_id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return event_crud.create_event(session, player_id, event_in)

@router.get("/{id}/events", response_model=list[EventIn])
def get_events_by_id(player_id: int, session: Session = Depends(get_session)):
    return event_crud.get_events_by_id(session, player_id)