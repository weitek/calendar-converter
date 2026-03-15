from typing import List, Dict, Any
from datetime import date, timedelta


def gregorian_to_julian(day: int, month: int, year: int) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в юлианскую.
    """
    results = []
    
    try:
        # Создаём григорианскую дату
        greg_date = date(year, month, day)
        
        # Вычисляем разницу в днях
        # Для дат после 1582 (введение григорианского календаря)
        # разница постепенно увеличивалась
        # 1582: 10 дней, 1700: 11 дней, 1800: 12 дней, 1900-2100: 13 дней
        
        if year >= 2100:
            offset = 14
        elif year >= 1900:
            offset = 13
        elif year >= 1800:
            offset = 12
        elif year >= 1700:
            offset = 11
        elif year >= 1582:
            offset = 10
        else:
            offset = 0
        
        # Вычитаем разницу
        julian_date = greg_date - timedelta(days=offset)
        
        results.append({
            "source": "fixed_offset",
            "value": {
                "day": julian_date.day,
                "month": julian_date.month,
                "year": julian_date.year,
                "offset_days": offset
            }
        })
    except Exception as e:
        results.append({
            "source": "fixed_offset",
            "value": None,
            "error": str(e)
        })
    
    return results


def julian_to_gregorian(day: int, month: int, year: int) -> List[Dict[str, Any]]:
    """
    Конвертирует юлианскую дату в григорианскую.
    """
    results = []
    
    try:
        # Создаём юлианскую дату
        julian_date = date(year, month, day)
        
        # Вычисляем разницу в днях
        if year >= 2100:
            offset = 14
        elif year >= 1900:
            offset = 13
        elif year >= 1800:
            offset = 12
        elif year >= 1700:
            offset = 11
        elif year >= 1582:
            offset = 10
        else:
            offset = 0
        
        # Прибавляем разницу
        greg_date = julian_date + timedelta(days=offset)
        
        results.append({
            "source": "fixed_offset",
            "value": {
                "day": greg_date.day,
                "month": greg_date.month,
                "year": greg_date.year,
                "offset_days": offset
            }
        })
    except Exception as e:
        results.append({
            "source": "fixed_offset",
            "value": None,
            "error": str(e)
        })
    
    return results


def convert_using_julian_lib_gregorian_to_julian(day: int, month: int, year: int) -> Dict[str, int]:
    """Упрощённая конвертация Gregorian -> Julian."""
    result = gregorian_to_julian(day, month, year)
    if result and result[0].get('value'):
        v = result[0]['value']
        return {"day": v['day'], "month": v['month'], "year": v['year']}
    return {"day": day, "month": month, "year": year}


def convert_using_julian_lib_julian_to_gregorian(day: int, month: int, year: int) -> Dict[str, int]:
    """Упрощённая конвертация Julian -> Gregorian."""
    result = julian_to_gregorian(day, month, year)
    if result and result[0].get('value'):
        v = result[0]['value']
        return {"day": v['day'], "month": v['month'], "year": v['year']}
    return {"day": day, "month": month, "year": year}
