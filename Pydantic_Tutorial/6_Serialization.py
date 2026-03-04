import json
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    zip_code: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'karachi' , 'state':'Sindh' ,'zip_code' : '775001'}

address1 = Address(**address_dict)

patient_dict = {'name':'Ali','gender' : 'male' , 'age' :35 ,'address':address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude=['name','gender'])

temp2 = patient1.model_dump_json(include=['name','address'])

print('Dict')
print(temp)
print(type(temp))

print('Json')
print(temp2)
print(type(temp2))