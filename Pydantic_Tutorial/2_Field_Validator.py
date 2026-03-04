from datetime import date
from typing import List, Dict, Optional, Annotated
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Invalid email domain: {domain_name}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if  0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")

def insert_patient(patient: Patient):
    print(patient)
    print(patient.name)
    print('inserted')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'John Doe', 'age': 30,'email':'john.doe@hdfc.com','linkedin_url':'https://www.linkedin.com/in/john-doe-1234567890', 'weight': 70.5, 'married': True, 'allergies': ['penicillin', 'latex'], 'contact': { 'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient(patient1)

