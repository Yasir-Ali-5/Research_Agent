from typing import TypedDict, List, Annotated
from operator import add
from pydantic import BaseModel
from typing import List, Optional

class Section(BaseModel):
    title: str
    description: Optional[str] = None
    sub_sections: Optional[List[str]] = None

class Sections(BaseModel):
    sections: List[Section]

class Outline(BaseModel):
  outline: str

class AgentState(TypedDict):
  input: str
  report_plan: list[Section]
  outline: str
  completed_sections: Annotated[list, add]
  report: str


class WriterState(TypedDict):
  section: Section
  completed_sections: Annotated[list, add]