from crewai import Crew, Process
from tasks import document_analysis_task, compliance_task, space_planning_task, material_selection_task, installation_guide_task
from agents import document_analyst, compliance_officer, space_planner, material_specialist, installation_architect
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the Crew
crew = Crew(
    agents=[document_analyst, compliance_officer, space_planner, material_specialist, installation_architect],
    tasks=[document_analysis_task, compliance_task, space_planning_task, material_selection_task, installation_guide_task],
    process=Process.sequential,
    verbose=True
)

# Kick off the workflow
result = crew.kickoff()

# Save the final guide
with open("installation_guide.md", "w") as f:
    f.write(result)

print("Installation guide saved to installation_guide.md") 