from typing import List, Dict, Any, Optional
import math


# Synodic month (лунный месяц) в днях
SYNODIC_MONTH = 29.53058867

# Известное новолуние (JD)
KNOWN_NEW_MOON_JD = 2451550.1  # 6 января 2000


def get_lunar_phase(
    day: int, 
    month: int, 
    year: int,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None
) -> List[Dict[str, Any]]:
    """
    Рассчитывает лунную фазу для заданной даты.
    Использует точные астрономические данные.
    """
    results = []
    
    try:
        # Вычисляем JD для даты
        a = (14 - month) // 12
        y = year + 4800 - a
        m = month + 12 * a - 3
        
        jd = day + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045 + 0.5
        
        # Вычисляем возраст луны (lunar age)
        days_since_new_moon = (jd - KNOWN_NEW_MOON_JD) % SYNODIC_MONTH
        lunar_day = int(days_since_new_moon) + 1
        
        # Вычисляем угол фазы (0-360)
        phase_angle = (days_since_new_moon / SYNODIC_MONTH) * 360
        phase_name = get_phase_name(phase_angle)
        
        # Вычисляем процент освещённости
        illumination = (1 - math.cos(math.radians(phase_angle))) / 2 * 100
        
        # Вычисляем следующую основную фазу
        days_to_next = SYNODIC_MONTH - days_since_new_moon
        next_jd = jd + days_to_next
        next_phase_type = get_next_phase_type(phase_name)
        
        results.append({
            "source": "astronomical_calculations",
            "value": {
                "jd": jd,
                "lunar_day": lunar_day,
                "phase": phase_name,
                "phase_angle": round(phase_angle, 2),
                "illumination": round(illumination, 2),
                "next_phase": {
                    "type": next_phase_type,
                    "time_utc": format_jd(next_jd),
                    "jd": next_jd
                }
            }
        })
    except Exception as e:
        results.append({
            "source": "astronomical_calculations",
            "value": None,
            "error": str(e)
        })
    
    return results


def get_phase_name(angle: float) -> str:
    """Определяет название фазы по углу."""
    if angle < 11.25 or angle >= 348.75:
        return "New Moon"
    elif angle < 78.75:
        return "Waxing Crescent"
    elif angle < 101.25:
        return "First Quarter"
    elif angle < 168.75:
        return "Waxing Gibbous"
    elif angle < 191.25:
        return "Full Moon"
    elif angle < 258.75:
        return "Waning Gibbous"
    elif angle < 281.25:
        return "Last Quarter"
    elif angle < 348.75:
        return "Waning Crescent"
    else:
        return "New Moon"


def get_next_phase_type(current_phase: str) -> str:
    """Возвращает тип следующей фазы."""
    phase_order = [
        "New Moon",
        "First Quarter",
        "Full Moon",
        "Last Quarter"
    ]
    
    try:
        idx = phase_order.index(current_phase)
        return phase_order[(idx + 1) % 4]
    except ValueError:
        return "First Quarter"


def format_jd(jd: float) -> str:
    """Конвертирует JD в строку ISO формата UTC."""
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
    
    # Вычисляем время
    fractional_day = f
    hours = int(fractional_day * 24)
    minutes = int((fractional_day * 24 - hours) * 60)
    seconds = int(((fractional_day * 24 - hours) * 60 - minutes) * 60)
    
    return f"{year:04d}-{month:02d}-{day:02d}T{hours:02d}:{minutes:02d}:{seconds:02d}Z"


def get_lunar_phase_simple(
    day: int, 
    month: int, 
    year: int,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None
) -> Dict[str, Any]:
    """Упрощённый расчёт лунной фазы."""
    results = get_lunar_phase(day, month, year, latitude, longitude)
    
    if results and results[0].get('value'):
        return results[0]['value']
    
    return {
        "jd": 0,
        "lunar_day": 1,
        "phase": "Unknown",
        "illumination": 0,
        "next_phase": None
    }
