from crewai import Agent
from crewai_tools import FileReadTool, WebSearchTool
# from adk.tools import PdfParserTool, WebScraperTool  # Custom ADK tools

# Initialize tools
file_reader = FileReadTool()
web_search = WebSearchTool()

# Placeholder for ADK tools - these will need to be implemented in adk/tools.py
# and ADK needs to be installed and discoverable.
class PdfParserToolPlaceholder:
    def execute(self, file_path):
        print(f"Placeholder: PDF Parser would process {file_path}")
        return f"Parsed content of {file_path}"

class WebScraperToolPlaceholder:
    def execute(self, url):
        print(f"Placeholder: Web Scraper would process {url}")
        return f"Scraped content of {url}"

pdf_parser = PdfParserToolPlaceholder() # ADK tool for parsing PDFs
web_scraper = WebScraperToolPlaceholder() # ADK tool for scraping part sources

# Agent 1: Document Analyst
document_analyst = Agent(
    role="Document Analyst",
    goal="Extract and summarize key information from user manuals, part specifications, and heat/air principles",
    backstory="You are an expert technical analyst skilled at parsing complex documents and summarizing technical details clearly.",
    tools=[file_reader, pdf_parser],
    verbose=True,
    allow_delegation=False
)

# Agent 2: Compliance Officer
compliance_officer = Agent(
    role="Compliance Officer",
    goal="Ensure the installation complies with local ordinances and safety regulations",
    backstory="You are a regulatory expert familiar with building codes and safety standards, ensuring all plans meet legal requirements.",
    tools=[file_reader, pdf_parser],
    verbose=True,
    allow_delegation=False
)

# Agent 3: Space Planner
space_planner = Agent(
    role="Space Planner",
    goal="Analyze shed dimensions to determine optimal vent and piping placement",
    backstory="You are an architectural planner specializing in spatial analysis and HVAC system layouts.",
    tools=[file_reader],
    verbose=True,
    allow_delegation=False
)

# Agent 4: Material Specialist
material_specialist = Agent(
    role="Material Specialist",
    goal="Identify required materials and recommend sources for procurement",
    backstory="You are a procurement expert with deep knowledge of HVAC materials and supplier networks.",
    tools=[web_search, web_scraper],
    verbose=True,
    allow_delegation=True
)

# Agent 5: Installation Architect
installation_architect = Agent(
    role="Installation Architect",
    goal="Compile a comprehensive step-by-step installation guide",
    backstory="You are a seasoned HVAC engineer skilled at creating detailed, professional-grade installation plans.",
    verbose=True,
    allow_delegation=True
) 