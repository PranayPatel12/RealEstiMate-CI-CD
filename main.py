import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = joblib.load("decision_tree_model.pkl")
model_columns = joblib.load("model_columns.pkl")  # Load column order

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request,
    POSTED_BY: str = Form(...),
    UNDER_CONSTRUCTION: int = Form(...),
    RERA: int = Form(...),
    BHK_NO: int = Form(...),
    BHK_OR_RK: str = Form(...),
    SQUARE_FT: float = Form(...),
    READY_TO_MOVE: int = Form(...),
    RESALE: int = Form(...),
    LONGITUDE: float = Form(...),
    LATITUDE: float = Form(...)
):
    # Construct input as DataFrame
    input_dict = {
        "POSTED_BY": [POSTED_BY],
        "UNDER_CONSTRUCTION": [UNDER_CONSTRUCTION],
        "RERA": [RERA],
        "BHK_NO.": [BHK_NO],
        "BHK_OR_RK": [BHK_OR_RK],
        "SQUARE_FT": [SQUARE_FT],
        "READY_TO_MOVE": [READY_TO_MOVE],
        "RESALE": [RESALE],
        "LONGITUDE": [LONGITUDE],
        "LATITUDE": [LATITUDE]
    }

    input_df = pd.DataFrame(input_dict)
    input_df = pd.get_dummies(input_df, drop_first=True)

    # Reindex to match training columns
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    return templates.TemplateResponse("form.html", {
        "request": request,
        "prediction": f"Predicted Price: ₹{round(prediction, 2)} Lakhs"
    })

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
