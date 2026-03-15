import pytest
from fastapi.testclient import TestClient


def test_widgets_endpoint():
    """Test widgets endpoint returns all calendars"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.get("/api/widgets")
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    # Проверяем, что все ожидаемые виджеты присутствуют
    ids = [w['id'] for w in data]
    
    expected = ['gregorian', 'julian', 'chinese', 'hebrew', 'julian_day', 'lunar_phase']
    for e in expected:
        assert e in ids


def test_widgets_structure():
    """Test structure of widget response"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.get("/api/widgets")
    
    data = response.json()
    
    # Проверяем структуру первого виджета
    widget = data[0]
    assert 'id' in widget
    assert 'name' in widget
    assert 'fields' in widget
    assert 'input_format' in widget
    assert 'supported_directions' in widget
