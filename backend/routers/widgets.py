from fastapi import APIRouter, Query
from typing import List, Dict, Any, Optional

from services.i18n import get_widget_names
from config import settings

router = APIRouter()


def get_widgets_config(language: str = "ru") -> List[Dict[str, Any]]:
    """Получить конфигурацию виджетов с учётом языка."""
    widget_names = get_widget_names(language)
    
    return [
        {
            "id": "gregorian",
            "name": widget_names["gregorian"],
            "fields": ["day", "month", "year"],
            "input_format": "gregorian",
            "supported_directions": ["from", "to"]
        },
        {
            "id": "julian",
            "name": widget_names["julian"],
            "fields": ["day", "month", "year"],
            "input_format": "julian",
            "supported_directions": ["from", "to"]
        },
        {
            "id": "chinese",
            "name": widget_names["chinese"],
            "fields": ["day", "month", "year", "is_leap"],
            "input_format": "chinese",
            "supported_directions": ["from", "to"]
        },
        {
            "id": "hebrew",
            "name": widget_names["hebrew"],
            "fields": ["day", "month", "year"],
            "input_format": "hebrew",
            "supported_directions": ["from", "to"]
        },
        {
            "id": "julian_day",
            "name": widget_names["julian_day"],
            "fields": ["jd"],
            "input_format": "jd",
            "supported_directions": ["to"]
        },
        {
            "id": "lunar_phase",
            "name": widget_names["lunar_phase"],
            "fields": [],
            "input_format": None,
            "supported_directions": ["to"]
        }
    ]


@router.get("/widgets")
async def get_widgets(lang: Optional[str] = Query(None)) -> List[Dict[str, Any]]:
    """
    Возвращает список доступных виджетов (календарей) и их конфигурацию.
    """
    language = lang if lang in ["ru", "en"] else settings.DEFAULT_LANGUAGE
    return get_widgets_config(language)
