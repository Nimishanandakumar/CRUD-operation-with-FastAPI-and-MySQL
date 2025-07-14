from sqlalchemy import Column, Integer, String
from database import Base

class Patient(Base):
    __tablename__ = "Patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    diagnosis = Column(String(255))
