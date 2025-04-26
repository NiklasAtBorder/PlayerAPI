from fastapi import HTTPException, status
from sqlmodel import Session, select
from .baseplayer import PlayerIn, PlayerDb, EventIn, EventDb

EventTypes = ["level_started", "level_solved"]

def create_player(session: Session, player_in: PlayerIn):
    player = PlayerDb.model_validate(player_in)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

def get_player(session: Session, name: str = ""):
    if name != "":
        return session.exec(select(PlayerDb).where(PlayerDb.name == name)).all()
    return session.exec(select(PlayerDb)).all()

def get_player_by_id(session: Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {player_id} not found."
        )
    events = session.exec(select(EventDb).where(EventDb.player_id == player_id)).all()
    player.events = events
    return player
    
def delete_player(session: Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(
            detail=f"Player with id {player_id} not found.", status_code=status.HTTP_404_NOT_FOUND
        )
    return {"message": f"Player with id {player_id} deleted."}

def create_event(session: Session, player_id: int, event_in: EventIn):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(
            detail=f"Player with id {player_id} not found.", status_code=status.HTTP_404_NOT_FOUND,
        )
    event = EventDb(**event_in.model_dump(), player_id=player_id)
    session.add(event)
    session.commit()
    session.refresh(event)
    return event

def get_events(session: Session, player_id: int):
    events = session.exec(select(EventDb).where(EventDb.player_id == player_id)).all()
    return events

