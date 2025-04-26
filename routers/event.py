from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..db.baseplayer import EventIn
from ..db.database import get_session
from ..db import event_crud

router = APIRouter(prefix="/event", tags=["event"])


@router.post("/players/{id}/events", status_code=status.HTTP_201_CREATED)
def create_event(player_id: int, event_in: EventIn, session: Session = Depends(get_session)):
    return event_crud.create_event(session, player_id, event_in)

@router.get("/players/{id}/events", response_model=list[EventIn])
def get_events(player_id: int, session: Session = Depends(get_session)):
    return event_crud.get_events(session, player_id)