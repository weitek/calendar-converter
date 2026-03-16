from typing import Dict

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "ru": {
        "gregorian": "Григорианский",
        "julian": "Юлианский",
        "chinese": "Китайский",
        "hebrew": "Еврейский",
        "julian_day": "Julian Day",
        "lunar_phase": "Лунный",
        "new_moon": "Новолуние",
        "waxing_crescent": "Растущий серп",
        "first_quarter": "Первая четверть",
        "waxing_gibbous": "Растущая выпуклая",
        "full_moon": "Полнолуние",
        "waning_gibbous": "Убывающая выпуклая",
        "last_quarter": "Последняя четверть",
        "waning_crescent": "Убывающий серп",
        "lunar_day": "Лунный день",
        "phase": "Фаза",
        "illumination": "Освещённость",
        "next_phase": "Следующая фаза",
        "jd": "JD",
        "as_source": "Как источник",
        "as_target": "Как цель",
        "source": "Источник",
        "target": "Цель",
        "recalculate": "Пересчитать",
        "loading": "Загрузка...",
        "day": "День",
        "month": "Месяц",
        "year": "Год",
    },
    "en": {
        "gregorian": "Gregorian",
        "julian": "Julian",
        "chinese": "Chinese",
        "hebrew": "Hebrew",
        "julian_day": "Julian Day",
        "lunar_phase": "Lunar",
        "new_moon": "New Moon",
        "waxing_crescent": "Waxing Crescent",
        "first_quarter": "First Quarter",
        "waxing_gibbous": "Waxing Gibbous",
        "full_moon": "Full Moon",
        "waning_gibbous": "Waning Gibbous",
        "last_quarter": "Last Quarter",
        "waning_crescent": "Waning Crescent",
        "lunar_day": "Lunar Day",
        "phase": "Phase",
        "illumination": "Illumination",
        "next_phase": "Next Phase",
        "jd": "JD",
        "as_source": "As source",
        "as_target": "As target",
        "source": "Source",
        "target": "Target",
        "recalculate": "Recalculate",
        "loading": "Loading...",
        "day": "Day",
        "month": "Month",
        "year": "Year",
    },
}

LUNAR_PHASE_TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "ru": {
        "New Moon": "Новолуние",
        "Waxing Crescent": "Растущий серп",
        "First Quarter": "Первая четверть",
        "Waxing Gibbous": "Растущая выпуклая",
        "Full Moon": "Полнолуние",
        "Waning Gibbous": "Убывающая выпуклая",
        "Last Quarter": "Последняя четверть",
        "Waning Crescent": "Убывающий серп",
    },
    "en": {
        "New Moon": "New Moon",
        "Waxing Crescent": "Waxing Crescent",
        "First Quarter": "First Quarter",
        "Waxing Gibbous": "Waxing Gibbous",
        "Full Moon": "Full Moon",
        "Waning Gibbous": "Waning Gibbous",
        "Last Quarter": "Last Quarter",
        "Waning Crescent": "Waning Crescent",
    },
}


def get_translation(key: str, lang: str = "ru") -> str:
    """Получить перевод по ключу."""
    if lang not in TRANSLATIONS:
        lang = "ru"
    return TRANSLATIONS.get(lang, TRANSLATIONS["ru"]).get(key, key)


def translate_phase(phase_name: str, lang: str = "ru") -> str:
    """Перевести название фазы луны."""
    if lang not in LUNAR_PHASE_TRANSLATIONS:
        lang = "ru"
    return LUNAR_PHASE_TRANSLATIONS.get(lang, LUNAR_PHASE_TRANSLATIONS["ru"]).get(phase_name, phase_name)


def get_widget_names(lang: str = "ru") -> Dict[str, str]:
    """Получить названия виджетов для указанного языка."""
    if lang not in TRANSLATIONS:
        lang = "ru"
    return {
        "gregorian": TRANSLATIONS[lang]["gregorian"],
        "julian": TRANSLATIONS[lang]["julian"],
        "chinese": TRANSLATIONS[lang]["chinese"],
        "hebrew": TRANSLATIONS[lang]["hebrew"],
        "julian_day": TRANSLATIONS[lang]["julian_day"],
        "lunar_phase": TRANSLATIONS[lang]["lunar_phase"],
    }
