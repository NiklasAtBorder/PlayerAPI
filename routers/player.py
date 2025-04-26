from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..db.baseplayer import PlayerIn, PlayerDb, EventIn
from ..db.database import get_session
from ..db import player_crud


router = APIRouter(prefix="/player", tags=["player"])

@router.post("/players", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerIn, session: Session = Depends(get_session)):
    return player_crud.create_player(session, player_in)

@router.get("/players", response_model=list[PlayerDb])
def get_player(name: str = "", session: Session = Depends(get_session)):
    return player_crud.get_player(session, name)

@router.get("/players/{id}", response_model=PlayerDb)
def get_player_by_id(player_id: int, session: Session = Depends(get_session)):
    return player_crud.get_player_by_id(session, player_id)
