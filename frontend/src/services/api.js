const API_BASE = '/api';

export async function fetchWidgets(language = 'ru') {
  const response = await fetch(`${API_BASE}/widgets?lang=${language}`);
  if (!response.ok) {
    throw new Error('Failed to fetch widgets');
  }
  return response.json();
}

export async function convertDate(sourceId, targetId, date, coordinates = {}, language = 'ru') {
  let endpoint = '';
  let payload = {};

  // Конвертация из Julian Day в другие календари
  if (sourceId === 'julian_day') {
    const jdValue = typeof date === 'number' ? date : date.jd;
    if (targetId === 'gregorian') {
      endpoint = '/convert/from-jd';
      payload = { jd: jdValue };
    } else {
      // Сначала конвертируем JD в gregorian
      const response = await fetch(`${API_BASE}/convert/from-jd`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ jd: jdValue })
      });
      const results = await response.json();
      const gregorianDate = results[0]?.value;
      if (!gregorianDate) {
        throw new Error('Failed to convert from JD');
      }
      // Теперь конвертируем из gregorian в target
      return convertDate('gregorian', targetId, gregorianDate, coordinates, language);
    }
  } else if (targetId === 'julian') {
    endpoint = '/convert/to-julian';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else if (targetId === 'gregorian' && sourceId === 'julian') {
    endpoint = '/convert/from-julian';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else if (targetId === 'julian_day') {
    endpoint = '/convert/to-jd';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else if (targetId === 'hebrew') {
    endpoint = '/convert/to-hebrew';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else if (targetId === 'chinese') {
    endpoint = '/convert/to-chinese';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else if (targetId === 'lunar_phase') {
    endpoint = '/convert/to-lunar-phase';
    payload = {
      day: date.day,
      month: date.month,
      year: date.year,
      latitude: coordinates.lat,
      longitude: coordinates.lng,
      language: language
    };
  } else if (sourceId === 'gregorian') {
    // Прямая конвертация из gregorian в целевой календарь
    switch (targetId) {
      case 'julian':
        endpoint = '/convert/to-julian';
        break;
      case 'hebrew':
        endpoint = '/convert/to-hebrew';
        break;
      case 'chinese':
        endpoint = '/convert/to-chinese';
        break;
      case 'julian_day':
        endpoint = '/convert/to-jd';
        break;
      case 'lunar_phase':
        endpoint = '/convert/to-lunar-phase';
        payload.latitude = coordinates.lat;
        payload.longitude = coordinates.lng;
        payload.language = language;
        break;
      default:
        throw new Error(`Unknown target: ${targetId}`);
    }
    payload = {
      day: date.day,
      month: date.month,
      year: date.year
    };
  } else {
    // Сложный случай: source не gregorian, target не gregorian
    // Сначала конвертируем в gregorian
    let gregorianDate;
    
    if (sourceId === 'julian') {
      const response = await fetch(`${API_BASE}/convert/from-julian`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          day: date.day,
          month: date.month,
          year: date.year
        })
      });
      const results = await response.json();
      gregorianDate = results[0]?.value;
    } else if (sourceId === 'hebrew') {
      const response = await fetch(`${API_BASE}/convert/from-hebrew`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          day: date.day,
          month: date.month,
          year: date.year
        })
      });
      const results = await response.json();
      gregorianDate = results[0]?.value;
    } else if (sourceId === 'chinese') {
      const response = await fetch(`${API_BASE}/convert/from-chinese`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          day: date.day,
          month: date.month,
          year: date.year,
          is_leap: date.is_leap || false
        })
      });
      const results = await response.json();
      gregorianDate = results[0]?.value;
    }
    
    if (!gregorianDate) {
      throw new Error('Failed to convert to gregorian');
    }
    
    // Теперь конвертируем из gregorian в target
    return convertDate('gregorian', targetId, gregorianDate, coordinates, language);
  }

  const response = await fetch(`${API_BASE}${endpoint}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error(`Conversion failed: ${response.statusText}`);
  }

  const results = await response.json();
  
  // Берем первый результат (основной)
  if (results && results.length > 0) {
    const primaryResult = results[0].value;
    
    // Если есть несколько результатов от разных библиотек
    if (results.length > 1) {
      console.warn('Multiple sources returned different results:', results);
    }
    
    return primaryResult;
  }

  throw new Error('No results returned');
}

export async function getLunarPhase(day, month, year, coordinates = {}, language = 'ru') {
  const response = await fetch(`${API_BASE}/convert/to-lunar-phase`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      day,
      month,
      year,
      latitude: coordinates.lat,
      longitude: coordinates.lng,
      language: language
    })
  });

  if (!response.ok) {
    throw new Error('Failed to get lunar phase');
  }

  const results = await response.json();
  return results[0]?.value;
}
