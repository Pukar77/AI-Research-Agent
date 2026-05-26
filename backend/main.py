"""AI Research Assistant - Main Entry Point
Can run in two modes:
1. CLI Mode (default): Interactive research assistant
2. MCP Server Mode: For integration with Kiro, Claude Desktop, etc.
"""
import sys
import asyncio
from backend.src.server.app import mcp, research_assistant


def print_header():
    """Print welcome header"""
    print("\n" + "=" * 80)
    print("🔬 AI RESEARCH ASSISTANT")
    print("=" * 80)
    print("Powered by Tavily Search + Groq AI Summarization")
    print("=" * 80 + "\n")


def print_separator():
    """Print separator line"""
    print("\n" + "-" * 80 + "\n")


async def research(query: str, max_results: int = 5, citation_style: str = "APA"):
    """
    Perform research on a query
    
    Args:
        query: Research query
        max_results: Number of sources to search
        citation_style: Citation format (APA or MLA)
    """
    print(f"🔍 Researching: {query}")
    print(f"📊 Sources: {max_results}")
    print(f"📚 Citation Style: {citation_style}")
    print("\n⏳ Please wait, this may take 10-20 seconds...\n")
    
    try:
        # Perform research
        result = await research_assistant(
            query=query,
            max_results=max_results,
            citation_style=citation_style
        )
        
        # Check for errors
        if "error" in result:
            print(f"❌ Error: {result['error']}")
            return
        
        # Display results
        print_separator()
        print("📄 RESEARCH DOCUMENT")
        print_separator()
        print(result.get("markdown", "No markdown content available"))
        print_separator()
        
        # Display stats
        print("📊 RESEARCH STATISTICS")
        print_separator()
        print(f"✅ Total Sources: {result.get('total_sources', 0)}")
        print(f"📝 Summaries Generated: {len(result.get('summaries', []))}")
        print(f"📚 Citations Created: {len(result.get('citations', []))}")
        print(f"📅 Generated At: {result.get('generated_at', 'N/A')}")
        print_separator()
        
        # Save to file
        filename = f"research_{query.replace(' ', '_')[:30]}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result.get("markdown", ""))
        print(f"💾 Saved to: {filename}\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()


async def interactive_mode():
    """Run in interactive mode"""
    print_header()
    
    while True:
        try:
            # Get user input
            print("\n" + "=" * 80)
            query = input("🔍 Enter your research query (or 'quit' to exit): ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you for using AI Research Assistant!\n")
                break
            
            if not query:
                print("⚠️  Please enter a valid query.")
                continue
            
            # Optional: Ask for number of sources
            try:
                max_results_input = input("📊 Number of sources (default 5, press Enter to skip): ").strip()
                max_results = int(max_results_input) if max_results_input else 5
                max_results = max(1, min(max_results, 10))  # Limit between 1-10
            except ValueError:
                max_results = 5
            
            # Optional: Ask for citation style
            citation_input = input("📚 Citation style (APA/MLA, default APA, press Enter to skip): ").strip().upper()
            citation_style = citation_input if citation_input in ['APA', 'MLA'] else 'APA'
            
            # Perform research
            await research(query, max_results, citation_style)
            
        except KeyboardInterrupt:
            print("\n\n👋 Thank you for using AI Research Assistant!\n")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")


async def single_query_mode(query: str):
    """Run a single query"""
    print_header()
    await research(query, max_results=5, citation_style="APA")


def run_cli_mode():
    """Run in CLI mode (interactive or single query)"""
    if len(sys.argv) > 1:
        # Single query mode from command line
        query = " ".join(sys.argv[1:])
        asyncio.run(single_query_mode(query))
    else:
        # Interactive mode
        asyncio.run(interactive_mode())


def run_server_mode():
    """Run in MCP server mode"""
    print("\n" + "=" * 80)
    print("🚀 Starting MCP Server Mode")
    print("=" * 80)
    print("Server will run on stdio transport for MCP clients")
    print("(Kiro, Claude Desktop, etc.)")
    print("=" * 80 + "\n")
    mcp.run()


def main():
    """Main entry point - decides which mode to run"""
    
    # Check if --server flag is provided
    if "--server" in sys.argv:
        run_server_mode()
    else:
        run_cli_mode()


if __name__ == "__main__":
    main()
