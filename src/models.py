# Importing all nessecary packages
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, model_validator

# Creating class to verify lead
class Lead(BaseModel):
    #For developement purposes, we will start with just these 5 parameters
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
            raise ValueError(f"minBudget must be less than $100,000,000: {value}")
        return value
    
    @model_validator(mode="after")
    def budgetCrossValidation(self):
        if self.maxBudget < self.minBudget:
            raise ValueError(f"minBudget cant be higher than maxBudget")
        return self


#Hard coding a test case
try:
    testLead = Lead(
        name = "Viraj",
        email = "virajboj@gmail.com",
        minBudget = 1000,
        maxBudget = 100,
        location = "USA"
    )

    print(testLead.name)
    print(testLead.email)
    print(testLead.minBudget)
    print(testLead.maxBudget)
    print(testLead.location)

except ValidationError as e:
    for x in e.errors():
        print("Lead blocked by firewall:", x["msg"])


