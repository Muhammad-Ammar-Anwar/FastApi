from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse 
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

import json

import pydantic

app = FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data, f)

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the Patient')]
    name: Annotated[str, Field(..., description='Name of the Patient')]
    city: Annotated[str, Field(..., description='City where the Patient is living')]
    age: Annotated[int, Field(..., gt=0,lt=120,description='Age of the Patient')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0,description='height of the Patient')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the Patient')]



    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        
        elif self.bmi <25:
            return 'Normal'
        
        elif self.bmi < 30:
            return 'Acceptable Weight'

        else:
            return 'Obese'

class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None,gt=0)]
    gender: Annotated[Optional[Literal['male','female','others']],Field(default=None)]
    height: Annotated[Optional[float], Field(default=None,gt=0)]
    weight: Annotated[Optional[float], Field(default=None,gt=0)]
    
@app.get('/view')
def view():
    data = load_data()

    return data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    # check whether the patient already exits
    if patient.id in data:
        return HTTPException(status_code=400, detail='Patient already exists')

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the save file 
    save_data(data)

    return JSONResponse(status_code=201, content={'message' : 'patient created Successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key] = value
    

    existing_patient_info['id'] = patient_id

    patient_pydantic_obj = Patient(**existing_patient_info)

    patient_pydantic_obj.model_dump(exclude='id')

    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'patient_updated'})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})
