from fastapi import HTTPException, status
from sqlmodel import Session, select
from .baseplayer import PlayerDb, EventIn, EventDb

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