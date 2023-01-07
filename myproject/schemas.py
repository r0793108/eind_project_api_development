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
    teams: str


class SpelerCreate(SpelerBase):
    pass


class Speler(SpelerBase):
    id: int
    HasChampionsLeague: bool

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
    ChampionsYears: str


class TeamCreate(UserBase):
    name: str
    ChampionsYears: str


class Team(UserBase):
    id: int
    HasWonChampionsLeague: bool

    class Config:
        orm_mode = True
