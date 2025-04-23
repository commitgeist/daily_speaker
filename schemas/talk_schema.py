from pydantic import BaseModel
from typing import List

class DeveloperInput(BaseModel):
    name: str
    done: List[str]
    todo: List[str]
    blockers: List[str]

class TalkOutput(BaseModel):
    message: str