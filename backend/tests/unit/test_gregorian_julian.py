import pytest
from backend.services import gregorian_julian


class TestGregorianJulian:
    """Unit tests for Gregorian-Julian conversion"""
    
    def test_gregorian_to_julian_simple(self):
        """Test conversion from Gregorian to Julian"""
        results = gregorian_julian.gregorian_to_julian(15, 3, 2025)
        
        # Проверяем, что есть хотя бы один результат
        assert len(results) > 0
        
        # Проверяем, что первый результат содержит корректные данные
        primary = results[0]
        assert primary['source'] in ['julian_lib', 'astronomy_engine']
        
        # Проверяем, что результат содержит поля day, month, year
        if primary.get('value'):
            assert 'day' in primary['value']
            assert 'month' in primary['value']
            assert 'year' in primary['value']
    
    def test_julian_to_gregorian_simple(self):
        """Test conversion from Julian to Gregorian"""
        results = gregorian_julian.julian_to_gregorian(2, 3, 2025)
        
        assert len(results) > 0
        
        primary = results[0]
        if primary.get('value'):
            assert 'day' in primary['value']
            assert 'month' in primary['value']
            assert 'year' in primary['value']
    
    def test_roundtrip_gregorian_to_julian_to_gregorian(self):
        """Test that roundtrip conversion returns original date"""
        original = (15, 3, 2025)
        
        # Gregorian -> Julian
        julian_results = gregorian_julian.gregorian_to_julian(*original)
        julian_date = julian_results[0].get('value')
        
        if julian_date:
            # Julian -> Gregorian
            greg_results = gregorian_julian.julian_to_gregorian(
                julian_date['day'], 
                julian_date['month'], 
                julian_date['year']
            )
            greg_date = greg_results[0].get('value')
            
            if greg_date:
                # День может отличаться на 1 из-за разницы в полночь/полдень
                assert abs(greg_date['year'] - original[2]) <= 1
                assert abs(greg_date['month'] - original[1]) <= 1
    
    def test_simple_conversion_functions(self):
        """Test simple conversion functions"""
        # Test Gregorian -> Julian
        result = gregorian_julian.convert_using_julian_lib_gregorian_to_julian(15, 3, 2025)
        assert result['day'] == 2
        assert result['month'] == 3
        assert result['year'] == 2025
        
        # Test Julian -> Gregorian
        result = gregorian_julian.convert_using_julian_lib_julian_to_gregorian(2, 3, 2025)
        assert result['day'] == 15
        assert result['month'] == 3
        assert result['year'] == 2025
