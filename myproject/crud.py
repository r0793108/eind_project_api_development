from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import models
import schemas


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_spelers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Speler).offset(skip).limit(limit).all()


def create_speler(db: Session, item: schemas.Team, user_id: int):
    db_speler = models.Team(**item.dict(), HisTeam_id=team_id)
    db.add(db_speler)
    db.commit()
    db.refresh(db_speler)
    return db_speler


def get_speler(db: Session, speler_id: int):
    return db.query(models.Speler).filter(models.Speler.id == speler_id).first()


def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teams).offset(skip).limit(limit).all()


def create_team(db: Session, user: schemas.UserCreate):
    db_team = models.Team(TeamName=team.TeamName, years=team.years)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

