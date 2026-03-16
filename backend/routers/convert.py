from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any, Optional

from models import (
    DateModel, 
    HebrewDateModel, 
    ChineseDateModel, 
    JDModel,
    LunarPhaseRequestModel,
    ResultWithSource
)
from services import gregorian_julian, jd, hebrew, lunar_phase, chinese
from config import settings

router = APIRouter()


@router.post("/convert/to-julian")
async def convert_to_julian(data: DateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в юлианскую.
    """
    return gregorian_julian.gregorian_to_julian(data.day, data.month, data.year)


@router.post("/convert/from-julian")
async def convert_from_julian(data: DateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует юлианскую дату в григорианскую.
    """
    return gregorian_julian.julian_to_gregorian(data.day, data.month, data.year)


@router.post("/convert/to-jd")
async def convert_to_jd(data: DateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в Юлианский день.
    """
    return jd.to_jd(data.day, data.month, data.year)


@router.post("/convert/from-jd")
async def convert_from_jd(data: JDModel) -> List[Dict[str, Any]]:
    """
    Конвертирует Юлианский день в григорианскую дату.
    """
    return jd.from_jd(data.jd)


@router.post("/convert/to-hebrew")
async def convert_to_hebrew(data: DateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в еврейскую.
    """
    return hebrew.to_hebrew(data.day, data.month, data.year)


@router.post("/convert/from-hebrew")
async def convert_from_hebrew(data: HebrewDateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует еврейскую дату в григорианскую.
    """
    return hebrew.from_hebrew(data.day, data.month, data.year)


@router.post("/convert/to-chinese")
async def convert_to_chinese(data: DateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в китайскую.
    """
    return await chinese.to_chinese(data.day, data.month, data.year)


@router.post("/convert/from-chinese")
async def convert_from_chinese(data: ChineseDateModel) -> List[Dict[str, Any]]:
    """
    Конвертирует китайскую дату в григорианскую.
    """
    return await chinese.from_chinese(data.day, data.month, data.year, data.is_leap)


@router.post("/convert/to-lunar-phase")
async def convert_to_lunar_phase(data: LunarPhaseRequestModel) -> List[Dict[str, Any]]:
    """
    Рассчитывает лунную фазу для заданной григорианской даты.
    """
    latitude = data.latitude if data.latitude is not None else settings.DEFAULT_LATITUDE
    longitude = data.longitude if data.longitude is not None else settings.DEFAULT_LONGITUDE
    language = data.language if data.language else settings.DEFAULT_LANGUAGE
    
    return lunar_phase.get_lunar_phase(
        data.day, 
        data.month, 
        data.year,
        latitude,
        longitude,
        language
    )
