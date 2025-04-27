from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..db.baseplayer import EventIn
from ..db.database import get_session
from ..db import event_crud

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=list[EventIn])
def get_events(type: str = "", session: Session = Depends(get_session)):
    return event_crud.get_events(session, type)