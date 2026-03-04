from datetime import date
from typing import List, Dict, Optional, Annotated
from pydantic import BaseModel, EmailStr, AnyUrl, Field


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=20,
            title="name",
            description="The name of the patient",
            example="John Doe",
        ),
    ]
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: Annotated[float, Field(..., gt=0, lt=200, strict=True)]
    married: bool
    allergies: Optional[List[str]] = None
    contact: Dict[str, str]

def insert_patient(patient: Patient):
    print(patient)
    print(patient.name)
    print('inserted')

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'John Doe', 'age': 30,'email':'john.doe@example.com','linkedin_url':'https://www.linkedin.com/in/john-doe-1234567890', 'weight': 70.5, 'married': True, 'allergies': ['penicillin', 'latex'], 'contact': { 'phone': '123-456-7890'}}

patient1 = Patient(**patient_info)
update_patient(patient1)





















# Declare a variable as a str
# and get editor support inside the function
# def main(user_id: str):
#     return user_id


# # A Pydantic model
# class User(BaseModel):
#     id: int
#     name: str
#     joined: date


# my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

# second_user_data = {
#     "id": 4,
#     "name": "Mary",
#     "joined": "2018-11-30",
# }

# my_second_user: User = User(**second_user_data)
# print(my_second_user)
# print(my_second_user.id)