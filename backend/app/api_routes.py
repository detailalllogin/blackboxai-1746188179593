from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .astrology import calculate_planetary_positions, datetime_to_julian_day
from .pdf_generator import create_kundli_pdf

router = APIRouter()

class KundliInput(BaseModel):
    name: str
    dob: str  # Date of birth in ISO format yyyy-mm-dd
    time: str  # Time of birth in HH:MM format
    place: str  # Place of birth (for geolocation, can be extended)

@router.post("/generate-kundli")
async def generate_kundli(data: KundliInput):
    try:
        dt_str = f"{data.dob} {data.time}"
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        jd_ut = datetime_to_julian_day(dt)
        planetary_positions = calculate_planetary_positions(jd_ut)
        # Additional astrology calculations can be added here

        # Generate PDF report
        pdf_filename = create_kundli_pdf(
            user_data={"name": data.name, "dob": data.dob, "time": data.time, "place": data.place},
            planetary_data=planetary_positions
        )

        return {
            "planetary_positions": planetary_positions,
            "pdf_report": pdf_filename
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Placeholder for AI Q&A rule-based endpoint
