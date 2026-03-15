from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter()

# Список доступных виджетов (календарей)
WIDGETS_CONFIG = [
    {
        "id": "gregorian",
        "name": "Григорианский",
        "fields": ["day", "month", "year"],
        "input_format": "gregorian",
        "supported_directions": ["from", "to"]
    },
    {
        "id": "julian",
        "name": "Юлианский",
        "fields": ["day", "month", "year"],
        "input_format": "julian",
        "supported_directions": ["from", "to"]
    },
    {
        "id": "chinese",
        "name": "Китайский",
        "fields": ["day", "month", "year", "is_leap"],
        "input_format": "chinese",
        "supported_directions": ["from", "to"]
    },
    {
        "id": "hebrew",
        "name": "Еврейский",
        "fields": ["day", "month", "year"],
        "input_format": "hebrew",
        "supported_directions": ["from", "to"]
    },
    {
        "id": "julian_day",
        "name": "Julian Day",
        "fields": ["jd"],
        "input_format": "jd",
        "supported_directions": ["to"]
    },
    {
        "id": "lunar_phase",
        "name": "Лунный",
        "fields": [],  # только вывод
        "input_format": None,
        "supported_directions": ["to"]
    }
]

@router.get("/widgets")
async def get_widgets() -> List[Dict[str, Any]]:
    """
    Возвращает список доступных виджетов (календарей) и их конфигурацию.
    """
    return WIDGETS_CONFIG
