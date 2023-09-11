from fastapi import FastAPI, HTTPException, Query
import joblib
import pandas as pd
from pydantic import BaseModel
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

# Load the trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

class InputData(BaseModel):
    Gender: int
    Age: int
    AnnualIncome: int

class OutputData(BaseModel):
    SpendingScorePrediction: float

@app.post("/predict/", response_model=OutputData)
async def predict_score(data: InputData):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([data.dict()])

    # Make a prediction
    prediction = model.predict(input_df[["Age", "AnnualIncome", "Gender"]])[0]
    
    # Scale the prediction to the range [0, 100]
    scaled_prediction = scaler.transform([[prediction]])[0][0]
    
    return {"SpendingScorePrediction": scaled_prediction}
