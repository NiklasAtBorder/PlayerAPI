from fastapi import HTTPException, status
from sqlmodel import Session, select
from .baseplayer import PlayerDb, EventIn, EventDb

def create_event(session: Session, player_id: int, event_in: EventIn):
    allowed = ["level_started", "level_solved"]

    p = session.get(PlayerDb, player_id)
    if not p:
        raise HTTPException(
            detail=f"Player with id {player_id} not found.", status_code=status.HTTP_404_NOT_FOUND,
        )
    if event_in.type not in allowed:
        raise HTTPException(
            detail=f"Event type {event_in.type} not allowed.", status_code=status.HTTP_400_BAD_REQUEST,
        )
    if event_in.type in allowed:
        event_in.detail = f"{event_in.type} by Player id {player_id}"
    else:
        pass
    e = EventDb(**event_in.model_dump(), player_id=player_id)
    session.add(e)
    session.commit()
    session.refresh(e)
    return e


def get_events_by_id(session: Session, player_id: int):
    events = session.exec(select(EventDb).where(EventDb.player_id == player_id)).all()
    return events

def get_events(session: Session, type: str = ""):
    allowed = ["level_started", "level_solved"]

    if type == "":
        return session.exec(select(EventDb)).all()
    if type in allowed:
        return session.exec(select(EventDb).where(EventDb.type == type)).all()
    raise HTTPException(
        detail=f"Event type {type} not allowed.", status_code=status.HTTP_400_BAD_REQUEST,
    )
