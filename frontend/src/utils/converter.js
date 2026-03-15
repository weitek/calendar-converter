import julian from 'julian';

export function gregorianToJulian(day, month, year) {
  try {
    const gregDate = new Date(year, month - 1, day);
    const jd = julian.to_jd(gregDate);
    const julianDate = julian.from_jd(jd);
    
    return {
      day: julianDate.getDate(),
      month: julianDate.getMonth() + 1,
      year: julianDate.getFullYear()
    };
  } catch (error) {
    console.error('Error in gregorianToJulian:', error);
    return { day, month, year };
  }
}

export function julianToGregorian(day, month, year) {
  try {
    const julDate = new Date(year, month - 1, day);
    const jd = julian.to_jd(julDate);
    const gregDate = julian.from_jd(jd);
    
    return {
      day: gregDate.getDate(),
      month: gregDate.getMonth() + 1,
      year: gregDate.getFullYear()
    };
  } catch (error) {
    console.error('Error in julianToGregorian:', error);
    return { day, month, year };
  }
}
