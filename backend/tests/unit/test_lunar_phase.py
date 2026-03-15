import pytest
from backend.services import lunar_phase


class TestLunarPhase:
    """Unit tests for lunar phase calculations"""
    
    def test_get_lunar_phase_2025(self):
        """Test lunar phase calculation for 2025"""
        results = lunar_phase.get_lunar_phase(15, 3, 2025)
        
        assert len(results) > 0
        
        primary = results[0]
        if primary.get('value'):
            value = primary['value']
            # Проверяем наличие обязательных полей
            assert 'jd' in value
            assert 'lunar_day' in value
            assert 'phase' in value
            assert 'illumination' in value
            # lunar_day должен быть от 1 до 30
            assert 1 <= value['lunar_day'] <= 30
            # illumination от 0 до 100
            assert 0 <= value['illumination'] <= 100
    
    def test_lunar_phase_different_dates(self):
        """Test lunar phase for different dates"""
        dates = [
            (1, 1, 2020),
            (15, 6, 2022),
            (31, 12, 2025)
        ]
        
        for day, month, year in dates:
            results = lunar_phase.get_lunar_phase(day, month, year)
            assert len(results) > 0
    
    def test_lunar_phase_with_coordinates(self):
        """Test lunar phase with custom coordinates"""
        results = lunar_phase.get_lunar_phase(
            15, 3, 2025,
            latitude=55.7558,  # Moscow
            longitude=37.6173
        )
        
        assert len(results) > 0
    
    def test_phase_name_function(self):
        """Test phase name determination"""
        # Тестируем различные углы фаз
        assert lunar_phase.get_phase_name(0) == "New Moon"
        assert lunar_phase.get_phase_name(90) == "First Quarter"
        assert lunar_phase.get_phase_name(180) == "Full Moon"
        assert lunar_phase.get_phase_name(270) == "Last Quarter"
        assert lunar_phase.get_phase_name(350) == "Waning Crescent"
    
    def test_simple_function(self):
        """Test simple lunar phase function"""
        result = lunar_phase.get_lunar_phase_simple(15, 3, 2025)
        
        assert 'jd' in result
        assert 'lunar_day' in result
        assert 'phase' in result
