from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    age: int
    diagnosis: str

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    patient_id: int

    class Config:
        orm_mode = True
