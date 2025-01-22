from pydantic import BaseModel

class FinalOutput(BaseModel):
  message: str
  