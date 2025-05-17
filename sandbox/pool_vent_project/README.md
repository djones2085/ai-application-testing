# Pool Shed Heater Vent Installation Guide - AI Agent Project

This project aims to develop a multi-agent system using CrewAI and Google Cloud's Agent Development Kit (ADK). The primary goal is to analyze various input materials (heater manuals, conversion kit manuals, shed dimensions, local ordinances, heat/air principles, and part links) to produce a comprehensive, step-by-step installation guide for a pool shed heater vent. The guide is intended for professionals who may be unfamiliar with this specific setup.

## Project Status Legend
- ⬜ Not Started
- 🟨 In Progress
- ✅ Complete

## 1. Local Development Environment Setup
- [⬜] **Python Installation**: Ensure Python 3.10–3.13 is installed.
- [✅] **Project Directory Structure**:
    - [✅] Main project directory: `pool_vent_project`
    - [✅] `main.py` (for CrewAI workflow)
    - [✅] `agents.py` (for CrewAI agent definitions)
    - [✅] `tasks.py` (for CrewAI task definitions)
    - [✅] `adk/` directory:
        - [✅] `adk/tools.py` (for custom ADK tool implementations)
        - [✅] `adk/workflow.py` (for ADK workflow definitions)
    - [✅] `data/` directory with placeholder files:
        - [✅] `heater_manual.pdf`
        - [✅] `conversion_kit_manual.pdf`
        - [✅] `shed_dimensions.txt`
        - [✅] `local_ordinances.pdf`
        - [✅] `heat_air_principles.pdf`
        - [✅] `part_links.txt`
- [⬜] **Python Virtual Environment**:
    - [⬜] Create virtual environment (e.g., `python3 -m venv .venv`).
    - [⬜] Activate virtual environment (e.g., `source .venv/bin/activate`).
- [⬜] **Install CrewAI & Dependencies**:
    - [⬜] `pip install crewai crewai-tools python-dotenv`
- [⬜] **Install Google ADK**:
    - [⬜] Clone ADK repository (`git clone https://github.com/google/adk`).
    - [⬜] Install ADK dependencies (`cd adk && pip install -r requirements.txt`).
    - [⬜] Set up Google Cloud Project:
        - [⬜] Select/Create GCP Project.
        - [⬜] Configure `gcloud init`.
        - [⬜] Enable Vertex AI API (`gcloud services enable aiplatform.googleapis.com`).
    - [⬜] Install ADK CLI (`python -m adk.cli.install`).
- [⬜] **Environment Variables**:
    - [⬜] Create `.env` file in the project root.
    - [⬜] Add `OPENAI_API_KEY` (if using OpenAI).
    - [⬜] Add GCP credentials (`GOOGLE_APPLICATION_CREDENTIALS`, `GEMINI_MODEL`, etc. if using Gemini).
- [⬜] **(Optional) Docker**: Install Docker for ADK's containerized local testing.
- [⬜] **Editor/IDE Configuration**: Configure to use the project's virtual environment interpreter.

## 2. CrewAI Agent and Task Definition
- [✅] **Define Agents in `agents.py`** (Initial placeholders complete, refinement needed):
    - [⬜] **Document Analyst**:
        - Goal: Extract/summarize info from manuals, specs, principles.
        - Backstory: Expert technical analyst.
        - Tools: `FileReadTool`, `PdfParserTool` (custom ADK tool).
    - [⬜] **Compliance Officer**:
        - Goal: Ensure compliance with local ordinances/safety regulations.
        - Backstory: Regulatory expert.
        - Tools: `FileReadTool`, `PdfParserTool` (custom ADK tool).
    - [⬜] **Space Planner**:
        - Goal: Analyze shed dimensions for vent/piping placement.
        - Backstory: Architectural planner for HVAC.
        - Tools: `FileReadTool`.
    - [⬜] **Material Specialist**:
        - Goal: Identify required materials and recommend sources.
        - Backstory: Procurement expert for HVAC materials.
        - Tools: `WebSearchTool`, `WebScraperTool` (custom ADK tool).
    - [⬜] **Installation Architect**:
        - Goal: Compile comprehensive step-by-step installation guide.
        - Backstory: Seasoned HVAC engineer.
        - Tools: (None specified initially, may need tools to format output).
- [✅] **Define Tasks in `tasks.py`** (Initial placeholders complete, refinement needed):
    - [⬜] **Document Analysis Task**:
        - Description: Parse and summarize manuals, principles. Extract specs/requirements.
        - Expected Output: Bullet-point summary.
        - Agent: Document Analyst.
    - [⬜] **Compliance Task**:
        - Description: Analyze local ordinances. Note restrictions/requirements.
        - Expected Output: Report on compliance requirements.
        - Agent: Compliance Officer.
    - [⬜] **Space Planning Task**:
        - Description: Analyze shed dimensions, recommend vent/piping placement.
        - Expected Output: Text-based diagram and description.
        - Agent: Space Planner.
    - [⬜] **Material Selection Task**:
        - Description: Identify materials, recommend sources, include part numbers/links.
        - Expected Output: Detailed list of materials with sources.
        - Agent: Material Specialist.
        - Context: Document Analysis, Compliance, Space Planning tasks.
    - [⬜] **Installation Guide Task**:
        - Description: Compile step-by-step guide with materials, safety, instructions.
        - Expected Output: Comprehensive Markdown document.
        - Agent: Installation Architect.
        - Context: All previous tasks.

## 3. Workflow Orchestration (`main.py`)
- [✅] **Initial `main.py` Setup** (Placeholder complete, refinement needed):
    - [⬜] Load environment variables using `python-dotenv`.
    - [⬜] Import agents and tasks.
    - [⬜] Define the `Crew` with agents, tasks, and `Process.sequential`.
    - [⬜] Implement `crew.kickoff()` to start the workflow.
    - [⬜] Write the result to `installation_guide.md`.
- [⬜] **Test `main.py` Execution**: Run `python main.py` and verify output.

## 4. ADK Integration and Custom Tools
- [⬜] **Implement Custom ADK Tools in `adk/tools.py`**:
    - [⬜] `PdfParserTool`: Implement PDF parsing logic (e.g., using PyPDF2, pdfplumber).
    - [⬜] `WebScraperTool`: Implement web scraping logic (e.g., using BeautifulSoup, requests-html).
- [⬜] **Update `agents.py`**:
    - [⬜] Replace placeholder tool instances with actual ADK custom tools.
- [⬜] **(Optional) Explore ADK Scaffolding**:
    - [⬜] Use `adk.cli.create --template multi-agent --output pool_vent_project/adk` to generate ADK template.
    - [⬜] Review and integrate useful parts into `adk/workflow.py` or `adk/tools.py`.
- [⬜] **ADK Local Development UI**:
    - [⬜] Run ADK local server (e.g., `adk.cli.serve --project pool_vent_project` or `adk serve --project_dir .`).
    - [⬜] Test agent states, logs, and outputs via the Web UI (typically `http://localhost:8080`).
- [⬜] **ADK CLI Testing**:
    - [⬜] Test individual tasks (e.g., `adk.cli.test --task document_analysis_task`).
    - [⬜] Test full workflow simulation (e.g., `adk.cli.run --workflow main.py`).

## 5. Running and Validation
- [⬜] **Initial Full Workflow Run**: Execute `python main.py`.
- [⬜] **Review Output**: Carefully review the generated `installation_guide.md`.
- [⬜] **(Optional) ADK Evaluation**:
    - [⬜] Use ADK evaluation tools (e.g., `adk.cli.evaluate --output installation_guide.md --test-cases compliance,safety,completeness`).
- [⬜] **Manual Review**: Obtain feedback from HVAC professionals on the guide's accuracy and completeness.

## 6. Project Enhancements & Next Steps
- [⬜] **Refine Agent Prompts & Backstories**: Optimize for better performance and clarity.
- [⬜] **Error Handling**: Improve robustness in agents, tasks, and tool integrations.
- [⬜] **Advanced Parsing**: Implement more sophisticated parsing for PDF and web content if needed.
- [⬜] **ADK Advanced Features**: Explore and potentially implement features like different workflow types, state management.
- [⬜] **"Plain English Translator" Agent**: Consider adding an agent to simplify technical language if required.
- [⬜] **`.gitignore` File**: Add a `.gitignore` to exclude `.venv/`, `__pycache__/`, `*.pyc`, `.env`, `installation_guide.md`, etc.
- [⬜] **(Future) Frontend Integration**: Consider a simple frontend (e.g., Streamlit) if interactive elements are desired.
- [⬜] **Documentation**: Maintain and update this README as the project progresses.
- [⬜] **Testing**: Implement unit and integration tests for agents, tools, and workflows. 