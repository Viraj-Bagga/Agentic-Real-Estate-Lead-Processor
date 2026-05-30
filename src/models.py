# Importing all nessecary packages
import json
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, model_validator
from src.memory import save_lead
from src.ai_processor import classify_lead
import chromadb
from src.logger import get_logger
logger = get_logger("models_module")


# Creating class to verify lead
class Lead(BaseModel):
    #For developement purposes, we will start with just these 5 parameters
    raw_message: str
    name: str
    email: EmailStr
    minBudget: float
    maxBudget: float
    location: str 

    #The reason we are checking budget is because if we already know that there is no property in our data base within the budget range, we can automatically reject the lead and make the pipeline more efficent
    @field_validator("minBudget")
    def validateMinBudget(cls, value):
        if value < 10:
            raise ValueError(f"minBudget must be greater than $10: {value}")
        return value
    
    @field_validator("maxBudget")
    def validateMaxBudget(cls, value):
        if value > 100000000:
            raise ValueError(f"maxBudget must be less than $100,000,000: {value}")
        return value
    
    @model_validator(mode="after")
    def budgetCrossValidation(self):
        if self.maxBudget < self.minBudget:
            raise ValueError(f"minBudget cant be higher than maxBudget")
        return self


#Reading lead data from a json file and then processing it


def processNewLead(filepath: str):
    try:
        with open(filepath, "r") as file:
            lead_data = json.load(file)
            lead = Lead(**lead_data)
            logger.info(f"SUCCESS: Lead {lead.name} validated.")
            return lead
    except ValidationError as e:
        error_msg = f"ERROR: Validation failed: {e.json()}"
        logger.error(error_msg)
        with open("src/errors.log", "a") as log_file:
            log_file.write(error_msg + "\n")
        return None
    except FileNotFoundError:
        logger.error("ERROR: File not found.")
        return None

def save_lead(lead: Lead, collection, status: str):
    collection.add(
        documents=[lead.raw_message],
        metadatas=[{"email": lead.email, "min": lead.minBudget, "max": lead.maxBudget, "status": status}],
        ids=[lead.email] 
    )
    print("SUCCESS: Lead stored with AI metadata.")

if __name__ == "__main__":
    client = chromadb.PersistentClient(path="src/chroma_db")
    collection = client.get_or_create_collection(name="real_estate_leads")

    lead = processNewLead("src/lead.json")
    
    if lead:
        classification = classify_lead(lead.raw_message)
        logger.info(f"AI CLASSIFICATION: {classification.urgency} - {classification.reasoning}")
        save_lead(lead, collection, classification.urgency)