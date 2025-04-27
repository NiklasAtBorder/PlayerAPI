from fastapi import HTTPException, status
from sqlmodel import Session, select
from .baseplayer import PlayerIn, PlayerDb

def create_player(session: Session, player_in: PlayerIn):
    p = PlayerDb.model_validate(player_in)
    session.add(p)
    session.commit()
    session.refresh(p)
    return p

def get_player(session: Session, name: str = ""):
    if name != "":
        return session.exec(select(PlayerDb).where(PlayerDb.name == name)).all()
    return session.exec(select(PlayerDb)).all()

def get_player_by_id(session: Session, player_id: int):
    player = session.get(PlayerDb, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Player with id {player_id} not found."
        )
    return player
    



