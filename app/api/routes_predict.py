from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key , get_current_user
from app.services.model_services import make_prediction


router = APIRouter()

class CarFeatures(BaseModel):
    company : str
    year : int
    owner : str
    fuel : str
    seller_type : str
    transmission : str
    km_driven : float
    mileage_mpg : float
    engine_cc : float
    max_power_bhp : float
    torque_nm : float
    seats : float


@router.post('/predict')
def predict_price(car : CarFeatures , user : str = Depends(get_current_user) , api_key : str = Depends(get_api_key)):
    prediction = make_prediction(car.model_dump())
    return {'predicted_price' : prediction}