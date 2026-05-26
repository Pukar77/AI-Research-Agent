"""Tests for MCP tools"""
import pytest
from unittest.mock import Mock, patch, AsyncMock
from src.tools.search_tool import SearchTool
from src.tools.summarize_tool import SummarizeTool
from src.tools.document_tool import DocumentTool
from src.models.schemas import SearchResult, Summary


@pytest.mark.asyncio
class TestSearchTool:
    """Test cases for SearchTool"""
    
    async def test_search_web_success(self):
        """Test successful web search"""
        tool = SearchTool()
        
        # Mock the tavily service
        mock_result = SearchResult(
            title="Test Title",
            url="https://example.com",
            content="Test content",
            score=0.95
        )
        
        with patch.object(tool.tavily_service, 'search', new_callable=AsyncMock) as mock_search:
            mock_search.return_value = [mock_result]
            
            results = await tool.search_web("test query", max_results=1)
            
            assert len(results) == 1
            assert results[0]["title"] == "Test Title"
            assert results[0]["url"] == "https://example.com"
            mock_search.assert_called_once_with("test query", 1)


@pytest.mark.asyncio
class TestSummarizeTool:
    """Test cases for SummarizeTool"""
    
    async def test_summarize_content_success(self):
        """Test successful content summarization"""
        tool = SummarizeTool()
        
        mock_summary = Summary(
            original_url="https://example.com",
            summary="Test summary",
            key_points=["Point 1", "Point 2"],
            word_count=10
        )
        
        with patch.object(tool.groq_service, 'summarize', new_callable=AsyncMock) as mock_summarize:
            mock_summarize.return_value = mock_summary
            
            result = await tool.summarize_content(
                title="Test",
                url="https://example.com",
                content="Test content"
            )
            
            assert result["url"] == "https://example.com"
            assert result["summary"] == "Test summary"
            assert len(result["key_points"]) == 2


@pytest.mark.asyncio
class TestDocumentTool:
    """Test cases for DocumentTool"""
    
    async def test_create_citation(self):
        """Test citation creation"""
        tool = DocumentTool()
        
        result = await tool.create_citation(
            title="Test Article",
            url="https://example.com",
            citation_style="APA"
        )
        
        assert "text" in result
        assert result["style"] == "APA"
        assert result["url"] == "https://example.com"
