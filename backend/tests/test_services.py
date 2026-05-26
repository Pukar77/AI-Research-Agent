"""Tests for service layer"""
import pytest
from unittest.mock import Mock, patch
from src.services.citation_service import CitationService
from src.models.schemas import SearchResult, CitationStyle


class TestCitationService:
    """Test cases for CitationService"""
    
    def test_format_apa_citation(self):
        """Test APA citation formatting"""
        service = CitationService()
        
        result = SearchResult(
            title="Test Article",
            url="https://example.com/article",
            content="Test content",
            published_date="2024-01-15"
        )
        
        citation = service.format_citation(result, CitationStyle.APA)
        
        assert citation.style == CitationStyle.APA
        assert "2024" in citation.text
        assert "Test Article" in citation.text
        assert citation.url == "https://example.com/article"
    
    def test_format_mla_citation(self):
        """Test MLA citation formatting"""
        service = CitationService()
        
        result = SearchResult(
            title="Test Article",
            url="https://example.com/article",
            content="Test content"
        )
        
        citation = service.format_citation(result, CitationStyle.MLA)
        
        assert citation.style == CitationStyle.MLA
        assert "Test Article" in citation.text
        assert "Accessed" in citation.text
        assert citation.url == "https://example.com/article"
    
    def test_format_multiple_citations(self):
        """Test formatting multiple citations"""
        service = CitationService()
        
        results = [
            SearchResult(
                title=f"Article {i}",
                url=f"https://example.com/article{i}",
                content="Content"
            )
            for i in range(3)
        ]
        
        citations = service.format_citations(results, CitationStyle.APA)
        
        assert len(citations) == 3
        assert all(c.style == CitationStyle.APA for c in citations)
