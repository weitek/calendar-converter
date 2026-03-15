import pytest
from fastapi.testclient import TestClient


def test_to_julian_endpoint():
    """Test /api/convert/to-julian endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/to-julian",
        json={"day": 15, "month": 3, "year": 2025}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
    # Проверяем структуру результата
    result = data[0]
    assert 'source' in result
    assert 'value' in result
    
    if result.get('value'):
        assert 'day' in result['value']
        assert result['value']['day'] == 2  # 15 Mar 2025 = 2 Mar 2025 (Julian)


def test_from_julian_endpoint():
    """Test /api/convert/from-julian endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/from-julian",
        json={"day": 2, "month": 3, "year": 2025}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_to_jd_endpoint():
    """Test /api/convert/to-jd endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/to-jd",
        json={"day": 1, "month": 1, "year": 2000}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
    # Проверяем, что JD близок к ожидаемому
    result = data[0]
    if result.get('value'):
        assert abs(result['value'] - 2451545.0) < 1


def test_from_jd_endpoint():
    """Test /api/convert/from-jd endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/from-jd",
        json={"jd": 2451545.0}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)


def test_to_hebrew_endpoint():
    """Test /api/convert/to-hebrew endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/to-hebrew",
        json={"day": 15, "month": 9, "year": 2023}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
    result = data[0]
    if result.get('value'):
        assert 'year' in result['value']
        assert result['value']['year'] == 5784


def test_to_lunar_phase_endpoint():
    """Test /api/convert/to-lunar-phase endpoint"""
    from backend.main import app
    
    client = TestClient(app)
    response = client.post(
        "/api/convert/to-lunar-phase",
        json={"day": 15, "month": 3, "year": 2025}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
    result = data[0]
    if result.get('value'):
        value = result['value']
        assert 'jd' in value
        assert 'lunar_day' in value
        assert 'phase' in value
        assert 'illumination' in value


def test_invalid_date_validation(self):
    """Test that invalid dates are rejected"""
    from backend.main import app
    
    client = TestClient(app)
    
    # Невалидная дата (32 дня)
    response = client.post(
        "/api/convert/to-julian",
        json={"day": 32, "month": 3, "year": 2025}
    )
    
    assert response.status_code == 422


def test_missing_fields_validation(self):
    """Test that missing fields are rejected"""
    from backend.main import app
    
    client = TestClient(app)
    
    # Неполные данные
    response = client.post(
        "/api/convert/to-julian",
        json={"day": 15, "month": 3}  # отсутствует year
    )
    
    assert response.status_code == 422
