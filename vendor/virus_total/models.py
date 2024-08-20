from pydantic import BaseModel, field_validator

from datetime import datetime


class Result(BaseModel):
    identifier: str
    type: str
    last_analysis_time: datetime
    is_malicious: bool

    @field_validator('is_malicious', mode='before')
    def _is_malicious(cls, value):
        return value != 0

