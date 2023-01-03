from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    TeamName = Column(String, index=True)
    ChampionsLeague = Column(Boolean, default=False)
    years = Column(String, index=True)

    spelers = relationship("Speler", back_populates="HisTeam")


class Speler(Base):
    __tablename__ = "spelers"

    id = Column(Integer, primary_key=True, index=True)
    SpelerName = Column(String, index=True)
    HasChampionsLeague = Column(Boolean, default=True)
    HisTeam_id = Column(Integer, ForeignKey("teams.id"))

    HisTeam = relationship("Team", back_populates="spelers")

