from typing import List, Dict, Any
import math


def to_jd(day: int, month: int, year: int) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в Юлианский день (JD).
    """
    results = []
    
    # Метод: ручной расчёт (формула для JD)
    try:
        a = (14 - month) // 12
        y = year + 4800 - a
        m = month + 12 * a - 3
        
        jd = day + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045
        jd_with_time = jd + 0.5  # для полуночи
        
        results.append({
            "source": "manual_formula",
            "value": jd_with_time
        })
    except Exception as e:
        results.append({
            "source": "manual_formula",
            "value": None,
            "error": str(e)
        })
    
    return results


def from_jd(jd: float) -> List[Dict[str, Any]]:
    """
    Конвертирует Юлианский день в григорианскую дату.
    """
    results = []
    
    # Метод: ручная формула
    try:
        z = int(jd + 0.5)
        f = jd + 0.5 - z
        
        if z < 2299161:
            a = z
        else:
            alpha = int((z - 1867216.25) / 36524.25)
            a = z + 1 + alpha - alpha // 4
        
        b = a + 1524
        c = int((b - 122.1) / 365.25)
        d = int(365.25 * c)
        e = int((b - d) / 30.6001)
        
        day = b - d - int(30.6001 * e)
        month = e - 1 if e < 14 else e - 13
        year = c - 4716 if month > 2 else c - 4715
        
        results.append({
            "source": "manual_formula",
            "value": {
                "day": day,
                "month": month,
                "year": year
            }
        })
    except Exception as e:
        results.append({
            "source": "manual_formula",
            "value": None,
            "error": str(e)
        })
    
    return results


def to_jd_simple(day: int, month: int, year: int) -> float:
    """Упрощённый расчёт JD."""
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    
    jd = day + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045
    return jd + 0.5


def from_jd_simple(jd: float) -> Dict[str, int]:
    """Упрощённый расчёт даты из JD."""
    z = int(jd + 0.5)
    f = jd + 0.5 - z
    
    if z < 2299161:
        a = z
    else:
        alpha = int((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - alpha // 4
    
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    
    day = b - d - int(30.6001 * e)
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    
    return {"day": day, "month": month, "year": year}
