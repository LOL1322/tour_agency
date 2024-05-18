from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(ModifyBaseModel):
    password: str


class LoginData(ModifyBaseModel):
    login: str
    password: str


class User(ModifyBaseModel):
    position: int
    login: str
    password: str


class Post(ModifyBaseModel):
    post: str
    power_level: int 
    

class Country(BaseModel):
    name: str


class Tour(BaseModel):
    country_id: int
    hours: int
    price: int


class Ticket(BaseModel):
    tour_id: int
    user_id: int
    date_start: str
    date_end: str