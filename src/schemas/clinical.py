from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PatientInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: Optional[str] = None
    dob: Optional[str] = None
    sex: Optional[str] = None
    mrn: Optional[str] = None


class Medication(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    dose: Optional[str] = None
    route: Optional[str] = None
    frequency: Optional[str] = None


class LabResult(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    value: Optional[str] = None
    unit: Optional[str] = None


class VitalSign(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    value: Optional[str] = None
    unit: Optional[str] = None


class ClinicalExtraction(BaseModel):
    model_config = ConfigDict(extra="ignore")

    patient: Optional[PatientInfo] = None
    diagnoses: List[str] = Field(default_factory=list)
    medications: List[Medication] = Field(default_factory=list)
    procedures: List[str] = Field(default_factory=list)
    allergies: List[str] = Field(default_factory=list)
    labs: List[LabResult] = Field(default_factory=list)
    vitals: List[VitalSign] = Field(default_factory=list)
    encounter_date: Optional[str] = None
    confidence: Optional[float] = None
