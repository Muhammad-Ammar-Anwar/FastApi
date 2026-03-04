from typing import List, Dict, Optional
from pydantic import BaseModel, EmailStr, computed_field


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: str
    height: float
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

def insert_patient(patient: Patient):
    print(patient)
    print(patient.name)
    print('inserted')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('BMI',patient.calculated_bmi)
    print('updated')


patient_info = {'name': 'John Doe', 'age': '67','email':'john.doe@hdfc.com','linkedin_url':'https://www.linkedin.com/in/john-doe-1234567890', 'height': 1.75, 'weight': 70.5, 'married': True, 'allergies': ['penicillin', 'latex'], 'contact_details': { 'phone': '123-456-7890','emergency_contact': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient(patient1)
