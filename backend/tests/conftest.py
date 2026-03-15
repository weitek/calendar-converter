import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    """Fixture for FastAPI test client"""
    return TestClient(app)


@pytest.fixture
def sample_date():
    """Sample Gregorian date for testing"""
    return {"day": 15, "month": 3, "year": 2025}


@pytest.fixture
def sample_hebrew_date():
    """Sample Hebrew date for testing"""
    return {"day": 1, "month": 1, "year": 5784}


@pytest.fixture
def sample_jd():
    """Sample Julian Day for testing"""
    return {"jd": 2451545.0}
