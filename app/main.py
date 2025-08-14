from fastapi import FastAPI, Depends
from app.schemas import PredicctOut, PredictIn
from app.deps import get_model
from app.health import router as health_router


app = FastAPI()
app.include_router(health_router)


@app.post("/predict", response_model=PredicctOut)
def predict(payload: PredictIn, model=Depends(get_model)):
    y = sum(payload.features) #placeholder for now
    return PredicctOut(prediction=y)