from typing import List, Dict, Optional
from pydantic import BaseModel, EmailStr, model_validator


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: str
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 65 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 65")
        return model



def insert_patient(patient: Patient):
    print(patient)
    print(patient.name)
    print('inserted')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')


patient_info = {'name': 'John Doe', 'age': '67','email':'john.doe@hdfc.com','linkedin_url':'https://www.linkedin.com/in/john-doe-1234567890', 'weight': 70.5, 'married': True, 'allergies': ['penicillin', 'latex'], 'contact_details': { 'phone': '123-456-7890','emergency_contact': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient(patient1)
