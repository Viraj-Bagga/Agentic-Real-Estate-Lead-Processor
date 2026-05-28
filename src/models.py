# Importing all nessecary packages
from pydantic import BaseModel

# Creating class to verify lead
class Lead(BaseModel):
    #For developement purposes, we will start with just these 5 parameters
    name: str
    email: str
    minBudget: float
    maxBudget: float
    location: str 



