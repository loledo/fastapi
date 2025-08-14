from pydantic import BaseModel, Field, conlist


class PredictIn(BaseModel):
    features: conlist(float, min_length=1) = Field(...)


class PredicctOut(BaseModel):
    prediction: float = Field(...)