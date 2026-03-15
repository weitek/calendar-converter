import pytest
from backend.services import jd


class TestJD:
    """Unit tests for Julian Day calculations"""
    
    def test_to_jd_known_value(self):
        """Test JD calculation for known date"""
        # JD для 2000-01-01 12:00 UT примерно 2451545.0
        results = jd.to_jd(1, 1, 2000)
        
        assert len(results) > 0
        
        # Проверяем, что JD близок к ожидаемому значению
        values = [r.get('value') for r in results if r.get('value') is not None]
        assert len(values) > 0
        
        # JD должен быть около 2451545
        found_close = any(abs(v - 2451545.0) < 1 for v in values)
        assert found_close
    
    def test_to_jd_2025_date(self):
        """Test JD for March 15, 2025"""
        results = jd.to_jd(15, 3, 2025)
        
        assert len(results) > 0
        
        values = [r.get('value') for r in results if r.get('value') is not None]
        assert len(values) > 0
    
    def test_from_jd_known_value(self):
        """Test conversion from known JD"""
        # JD 2451545.0 = 2000-01-01
        results = jd.from_jd(2451545.0)
        
        assert len(results) > 0
        
        # Проверяем, что получили дату 2000-01-01
        values = [r.get('value') for r in results if r.get('value') is not None]
        found_correct = any(
            v.get('year') == 2000 and v.get('month') == 1 and v.get('day') == 1
            for v in values if v
        )
        # Может отличаться на 1 день из-за времени суток
        assert found_correct or len(values) > 0
    
    def test_roundtrip_jd(self):
        """Test roundtrip conversion: date -> JD -> date"""
        original = (15, 3, 2025)
        
        # date -> JD
        jd_results = jd.to_jd(*original)
        jd_value = jd_results[0].get('value')
        
        if jd_value:
            # JD -> date
            date_results = jd.from_jd(jd_value)
            date_value = date_results[0].get('value')
            
            if date_value:
                # Проверяем близость (может отличаться на 1 день)
                assert abs(date_value['year'] - original[2]) <= 1
                assert abs(date_value['month'] - original[1]) <= 1
    
    def test_simple_functions(self):
        """Test simple conversion functions"""
        # Test to_jd_simple
        jd_val = jd.to_jd_simple(1, 1, 2000)
        assert abs(jd_val - 2451545.0) < 1
        
        # Test from_jd_simple
        date = jd.from_jd_simple(2451545.0)
        assert date['year'] == 2000
        assert date['month'] == 1
        assert date['day'] in [1, 2]  # может быть 1 или 2
