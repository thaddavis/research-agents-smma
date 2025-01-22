from pydantic import BaseModel
from datetime import datetime

class Interest(BaseModel):
  name: str

class Person(BaseModel):
  name: str
  description: str
  company: datetime
  interests: list[Interest]

class Attendees(BaseModel):
  people: list[Person]