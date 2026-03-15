from typing import List, Dict, Any, Optional
import httpx
from config import settings


async def to_chinese(day: int, month: int, year: int) -> List[Dict[str, Any]]:
    """
    Конвертирует григорианскую дату в китайскую.
    Вызывает Node.js сервис.
    """
    results = []
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.NODE_SERVICE_URL}/convert",
                json={
                    "type": "chinese",
                    "action": "to",
                    "day": day,
                    "month": month,
                    "year": year
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                results.append({
                    "source": "nodejs_lunar_javascript",
                    "value": data
                })
            else:
                results.append({
                    "source": "nodejs_lunar_javascript",
                    "value": None,
                    "error": f"HTTP {response.status_code}: {response.text}"
                })
    except httpx.ConnectError as e:
        results.append({
            "source": "nodejs_lunar_javascript",
            "value": None,
            "error": f"Connection error: {str(e)}"
        })
    except Exception as e:
        results.append({
            "source": "nodejs_lunar_javascript",
            "value": None,
            "error": str(e)
        })
    
    return results


async def from_chinese(day: int, month: int, year: int, is_leap: bool = False) -> List[Dict[str, Any]]:
    """
    Конвертирует китайскую дату в григорианскую.
    Вызывает Node.js сервис.
    """
    results = []
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.NODE_SERVICE_URL}/convert",
                json={
                    "type": "chinese",
                    "action": "from",
                    "day": day,
                    "month": month,
                    "year": year,
                    "is_leap": is_leap
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                data = response.json()
                results.append({
                    "source": "nodejs_lunar_javascript",
                    "value": data
                })
            else:
                results.append({
                    "source": "nodejs_lunar_javascript",
                    "value": None,
                    "error": f"HTTP {response.status_code}: {response.text}"
                })
    except httpx.ConnectError as e:
        results.append({
            "source": "nodejs_lunar_javascript",
            "value": None,
            "error": f"Connection error: {str(e)}"
        })
    except Exception as e:
        results.append({
            "source": "nodejs_lunar_javascript",
            "value": None,
            "error": str(e)
        })
    
    return results


async def to_chinese_simple(day: int, month: int, year: int) -> Optional[Dict[str, Any]]:
    """
    Упрощённая конвертация Gregorian -> Chinese.
    """
    results = await to_chinese(day, month, year)
    
    if results and results[0].get('value'):
        return results[0]['value']
    
    return None


async def from_chinese_simple(day: int, month: int, year: int, is_leap: bool = False) -> Optional[Dict[str, int]]:
    """
    Упрощённая конвертация Chinese -> Gregorian.
    """
    results = await from_chinese(day, month, year, is_leap)
    
    if results and results[0].get('value'):
        value = results[0]['value']
        return {
            "day": value.get('day', day),
            "month": value.get('month', month),
            "year": value.get('year', year)
        }
    
    return None
