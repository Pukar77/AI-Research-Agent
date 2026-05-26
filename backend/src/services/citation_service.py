"""Citation formatting service"""
from typing import List
from datetime import datetime
from urllib.parse import urlparse
from backend.src.models.schemas import Citation, CitationStyle, SearchResult


class CitationService:
    """Service for formatting citations in various styles"""
    
    def format_citation(
        self,
        search_result: SearchResult,
        style: CitationStyle = CitationStyle.APA
    ) -> Citation:
        """
        Format a citation for a search result
        
        Args:
            search_result: SearchResult to create citation for
            style: Citation style (APA or MLA)
            
        Returns:
            Citation object with formatted text
        """
        if style == CitationStyle.APA:
            citation_text = self._format_apa(search_result)
        elif style == CitationStyle.MLA:
            citation_text = self._format_mla(search_result)
        else:
            citation_text = self._format_apa(search_result)
        
        return Citation(
            text=citation_text,
            style=style,
            url=search_result.url
        )
    
    def _format_apa(self, result: SearchResult) -> str:
        """
        Format citation in APA style
        
        Format: Author/Site. (Year). Title. Retrieved from URL
        """
        # Extract domain as author
        domain = urlparse(result.url).netloc.replace("www.", "")
        
        # Get year from published_date or use current year
        year = "n.d."
        if result.published_date:
            try:
                year = result.published_date[:4]
            except:
                year = "n.d."
        
        # Format citation
        citation = f"{domain.capitalize()}. ({year}). {result.title}. Retrieved from {result.url}"
        
        return citation
    
    def _format_mla(self, result: SearchResult) -> str:
        """
        Format citation in MLA style
        
        Format: "Title." Site Name, URL. Accessed Date.
        """
        # Extract domain as site name
        domain = urlparse(result.url).netloc.replace("www.", "")
        
        # Get current date for access date
        access_date = datetime.now().strftime("%d %b. %Y")
        
        # Format citation
        citation = f'"{result.title}." {domain.capitalize()}, {result.url}. Accessed {access_date}.'
        
        return citation
    
    def format_citations(
        self,
        search_results: List[SearchResult],
        style: CitationStyle = CitationStyle.APA
    ) -> List[Citation]:
        """
        Format citations for multiple search results
        
        Args:
            search_results: List of SearchResult objects
            style: Citation style to use
            
        Returns:
            List of Citation objects
        """
        return [self.format_citation(result, style) for result in search_results]
