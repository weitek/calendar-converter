export function formatDate(day, month, year, format) {
  if (!day || !month || !year) return '--';
  
  const d = String(day).padStart(2, '0');
  const m = String(month).padStart(2, '0');
  const y = String(year);
  
  if (format === 'yyyy-mm-dd') {
    return `${y}-${m}-${d}`;
  }
  
  return `${d}.${m}.${y}`;
}

export function parseDate(dateString, format) {
  if (!dateString) return null;
  
  let day, month, year;
  
  if (format === 'yyyy-mm-dd') {
    const parts = dateString.split('-');
    if (parts.length !== 3) return null;
    [year, month, day] = parts;
  } else {
    const parts = dateString.split('.');
    if (parts.length !== 3) return null;
    [day, month, year] = parts;
  }
  
  return {
    day: parseInt(day),
    month: parseInt(month),
    year: parseInt(year)
  };
}

export function isValidDate(day, month, year) {
  const date = new Date(year, month - 1, day);
  return date.getFullYear() === year && 
         date.getMonth() === month - 1 && 
         date.getDate() === day;
}

export function getToday() {
  const today = new Date();
  return {
    day: today.getDate(),
    month: today.getMonth() + 1,
    year: today.getFullYear()
  };
}
