from pydantic import BaseModel


class TeamBase(BaseModel):
    TeamName: str
    ChampionsLeague: bool
    years: str | None = None


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    TeamName: str
    ChampionsLeague: bool
    years: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Team] = []

    class Config:
        orm_mode = True


class SpelerBase(BaseModel):
    SpelerName: str
    HasChampionsLeague: bool


class SpelerCreate(SpelerBase):
    pass


class Speler(SpelerBase):
    id: int
    SpelerName: str
    HisTeam_id: int

    class Config:
        orm_mode = True
