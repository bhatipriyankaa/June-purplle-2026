from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    event_id: str
    visitor_id: int
    camera_id: str
    event_type: str
    timestamp: datetime