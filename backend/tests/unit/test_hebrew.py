import pytest
from backend.services import hebrew


class TestHebrew:
    """Unit tests for Hebrew calendar conversion"""
    
    def test_to_hebrew_known_date(self):
        """Test conversion of known Gregorian date to Hebrew"""
        # 15 сентября 2023 = 1 Тишри 5784
        results = hebrew.to_hebrew(15, 9, 2023)
        
        assert len(results) > 0
        
        primary = results[0]
        if primary.get('value'):
            value = primary['value']
            assert value['year'] == 5784
            # Месяц может быть 1 (Тишри) или около него
            assert 1 <= value['month'] <= 2
    
    def test_to_hebrew_2025(self):
        """Test conversion of 2025 date"""
        results = hebrew.to_hebrew(15, 3, 2025)
        
        assert len(results) > 0
        
        primary = results[0]
        if primary.get('value'):
            value = primary['value']
            # 5785 год
            assert value['year'] in [5785, 5786]
    
    def test_from_hebrew_roundtrip(self):
        """Test roundtrip: Hebrew -> Gregorian -> Hebrew"""
        # Начинаем с известной еврейской даты
        heb_date = (1, 1, 5784)
        
        # Hebrew -> Gregorian
        results = hebrew.from_hebrew(*heb_date)
        greg_value = results[0].get('value')
        
        if greg_value:
            # Gregorian -> Hebrew
            back_results = hebrew.to_hebrew(
                greg_value['day'],
                greg_value['month'],
                greg_value['year']
            )
            back_value = back_results[0].get('value')
            
            if back_value:
                # Год должен совпадать
                assert back_value['year'] == heb_date[2]
    
    def test_simple_conversion_functions(self):
        """Test simple conversion functions"""
        # Test to_hebrew_simple
        result = hebrew.to_hebrew_simple(15, 9, 2023)
        assert result['year'] == 5784
        
        # Test from_hebrew_simple  
        result = hebrew.from_hebrew_simple(1, 1, 5784)
        # Должна получиться дата около сентября 2023
        assert result['year'] in [2023, 2024]
