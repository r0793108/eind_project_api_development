from pydantic import BaseModel


#class ItemBase(BaseModel):
#    title: str
#    description: str | None = None


#class ItemCreate(ItemBase):
#    pass


#class Item(ItemBase):
#    id: int
#    owner_id: int

#    class Config:
#        orm_mode = True


class SpelerBase(BaseModel):
    name: str
    club: str

class SpelerCreate(SpelerBase):
    pass


class Speler(SpelerBase):
    id: int
    HasChampionsLeague: bool
    club_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    #items: list[Item] = []

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    HasWonChampionsLeague: bool
    ChampionsYears: str
    

class TeamCreate(TeamBase):
    name: str
    ChampionsYears: str
    HasWonChampionsLeague: bool

class Team(TeamBase):
    id: int
    HasWonChampionsLeague: bool
    spelers: list[Speler] = []

    class Config:
        orm_mode = True
