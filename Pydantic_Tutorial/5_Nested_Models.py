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
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.zip_code)