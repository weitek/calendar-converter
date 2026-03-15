import pytest
from unittest.mock import patch, AsyncMock


class TestChinese:
    """Unit tests for Chinese calendar conversion"""
    
    @pytest.mark.asyncio
    async def test_to_chinese_mock(self):
        """Test conversion to Chinese with mocked Node.js"""
        mock_response = {
            "year": 2025,
            "month": 2,
            "day": 23,
            "is_leap": False,
            "chinese_year": "乙巳",
            "chinese_month": "二月",
            "chinese_day": "廿三"
        }
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_instance = AsyncMock()
            mock_instance.post.return_value.json.return_value = mock_response
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            from backend.services import chinese
            results = await chinese.to_chinese(15, 3, 2025)
            
            assert len(results) > 0
    
    @pytest.mark.asyncio
    async def test_from_chinese_mock(self):
        """Test conversion from Chinese with mocked Node.js"""
        mock_response = {
            "year": 2025,
            "month": 3,
            "day": 15
        }
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_instance = AsyncMock()
            mock_instance.post.return_value.json.return_value = mock_response
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            from backend.services import chinese
            results = await chinese.from_chinese(23, 2, 2025, False)
            
            assert len(results) > 0
    
    @pytest.mark.asyncio
    async def test_to_chinese_connection_error(self):
        """Test handling of connection error to Node.js"""
        with patch('httpx.AsyncClient') as mock_client:
            mock_instance = AsyncMock()
            mock_instance.post.side_effect = Exception("Connection refused")
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            from backend.services import chinese
            results = await chinese.to_chinese(15, 3, 2025)
            
            assert len(results) > 0
            # Должен быть error в результате
            assert results[0].get('error') is not None
