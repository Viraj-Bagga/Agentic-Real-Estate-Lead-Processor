# Importing all nessecary packages

import json
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, model_validator

# Creating class to verify lead
class Lead(BaseModel):
    #For developement purposes, we will start with just these 5 parameters
    name: str
    email: EmailStr
    minBudget: float
    maxBudget: float
    location: str 
    raw_message: str

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

with open("src/lead.json", "r") as file:    
    lead_data = json.load(file)
    
    try:
        testLead = Lead(**lead_data)
        print("Lead Approved")

        print(testLead.name)
        print(testLead.email)
        print(testLead.minBudget)
        print(testLead.maxBudget)
        print(testLead.location)
        print(testLead.raw_message)
    
    except ValidationError as e:

        for x in e.errors():
            print("Lead blocked by firewall:", x["msg"])        
            with open("src/errors.log", "a") as log_file:
                log_file.write(f"Lead blocked by firewall: {x['msg']}\n")
                
            exit(1)
