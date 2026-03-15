from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any

class DateModel(BaseModel):
    """Базовая модель даты (день, месяц, год)"""
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., gt=0)

class HebrewDateModel(BaseModel):
    """Модель для еврейской даты"""
    day: int = Field(..., ge=1, le=30)
    month: int = Field(..., ge=1, le=13)
    year: int = Field(..., gt=0)

    @validator('month')
    def validate_hebrew_month(cls, v):
        # Еврейские месяцы 1-13 (13 - Adar II в високосный год)
        if v < 1 or v > 13:
            raise ValueError('Месяц должен быть от 1 до 13')
        return v

class ChineseDateModel(BaseModel):
    """Модель для китайского календаря"""
    day: int = Field(..., ge=1, le=30)
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., gt=0)
    is_leap: bool = False

class JDModel(BaseModel):
    """Модель для Юлианского дня"""
    jd: float = Field(..., gt=0)

class LunarPhaseRequestModel(BaseModel):
    """Модель запроса лунных фаз"""
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    year: int = Field(..., gt=0)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ResultWithSource(BaseModel):
    """Результат с указанием источника"""
    source: str
    value: Any

class ConversionResponse(BaseModel):
    """Общая модель ответа конвертации"""
    results: List[ResultWithSource]

    def get_primary(self):
        """Возвращает первый результат как основной"""
        if self.results:
            return self.results[0].value
        return None

    def has_multiple(self) -> bool:
        """Проверяет, есть ли несколько различных результатов"""
        return len(self.results) > 1
