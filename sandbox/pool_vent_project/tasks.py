from crewai import Task
from agents import document_analyst, compliance_officer, space_planner, material_specialist, installation_architect

# Task 1: Analyze Documents
document_analysis_task = Task(
    description="Parse and summarize heater manual, conversion kit manual, and heat/air principles. Extract relevant specs and requirements.",
    expected_output="A bullet-point summary of key specifications, requirements, and principles.",
    agent=document_analyst
)

# Task 2: Check Compliance
compliance_task = Task(
    description="Analyze local ordinances and ensure the installation plan complies with regulations. Note any restrictions or requirements.",
    expected_output="A report listing compliance requirements and restrictions.",
    agent=compliance_officer
)

# Task 3: Plan Space
space_planning_task = Task(
    description="Analyze shed dimensions and recommend vent placement and piping routes. Consider safety and efficiency.",
    expected_output="A diagram (text-based) and description of vent and piping placement.",
    agent=space_planner
)

# Task 4: Select Materials
material_selection_task = Task(
    description="Identify required materials (e.g., exhaust piping, termination vents) and recommend online/local sources. Include part numbers and links.",
    expected_output="A detailed list of materials with sources, part numbers, and links.",
    agent=material_specialist,
    context=[document_analysis_task, compliance_task, space_planning_task]
)

# Task 5: Create Installation Guide
installation_guide_task = Task(
    description="Compile a step-by-step installation guide, including material usage, safety considerations, and professional instructions.",
    expected_output="A comprehensive Markdown document with numbered steps, material references, and safety notes.",
    agent=installation_architect,
    context=[document_analysis_task, compliance_task, space_planning_task, material_selection_task]
) 