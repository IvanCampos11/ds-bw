import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    # title: str = Field(..., example='water bike')
    # blurb: str = Field(..., example='A bike that floats')
    # goal: int = Field(..., example=5000)
    # launch_date: str = Field(..., example='08/06/2020')
    # deadline: str = Field(..., example='10/20/2020')
    # category: str = Field(..., example='sports')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `x1`: positive float
    - `x2`: integer
    - `x3`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """

    title: str = Field(..., example='water bike')
    blurb: str = Field(..., example='A bike that floats')
    goal: int = Field(..., example=5000)
    launch_date: str = Field(..., example='08/06/2020')
    deadline: str = Field(..., example='10/20/2020')
    category: str = Field(..., example='sports')
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
