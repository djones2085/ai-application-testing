import os
from dotenv import load_dotenv

# Explicitly load .env file from the current directory
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print(f"Warning: .env file not found at {dotenv_path}") # Or raise an error

import vertexai
from vertexai.preview import reasoning_engines
from vertexai import agent_engines
from multi_tool_agent.agent import root_agent # Assuming root_agent is in multi_tool_agent/agent.py

# Configuration
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")
# Ensure STAGING_BUCKET is not None and starts with "gs://"
if STAGING_BUCKET is None:
    raise ValueError("STAGING_BUCKET environment variable not set.")
if not STAGING_BUCKET.startswith("gs://"):
    STAGING_BUCKET = f"gs://{STAGING_BUCKET}"

vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET)

# app = reasoning_engines.AdkApp(agent=root_agent, enable_tracing=True)

# Read requirements from requirements_agent_engine.txt
with open("requirements_agent_engine.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip()]

AGENT_DISPLAY_NAME = "multi-tool-adk-agent-engine"
AGENT_DESCRIPTION = "ADK agent for multi-tool capabilities deployed via Agent Engine"

def deploy_agent():
    """Deploys the ADK agent to Vertex AI Agent Engine."""
    print(f"Initializing Vertex AI for project: {PROJECT_ID}, location: {LOCATION}, staging_bucket: {STAGING_BUCKET}")
    vertexai.init(
        project=PROJECT_ID,
        location=LOCATION,
        staging_bucket=STAGING_BUCKET,
    )

    print(f"Wrapping ADK agent: {root_agent.name} for Agent Engine deployment...")
    # The AdkApp class is used to package your ADK agent for Agent Engine.
    # It points to your core agent logic (root_agent).
    # app = reasoning_engines.AdkApp(
    #     agent=root_agent,
    #     # enable_tracing=True, # Optional: for better debugging in Vertex AI
    #     # You can specify the agent directory if it's not automatically discovered
    #     # based on the import of root_agent.
    #     # agent_dir="multi_tool_agent", # Usually not needed if import works
    # )

    print(f"Reading requirements from: {requirements}")

    print(f"Deploying agent '{AGENT_DISPLAY_NAME}' to Agent Engine...")
    print(f"This may take several minutes...")

    try:
        print(f"Attempting to deploy agent: {root_agent.name}")
        remote_app = agent_engines.create(
            agent_engine=root_agent,
            requirements=requirements,
            display_name="multi-tool-agent-adk",
            # extra_packages can be used if your agent has local Python sub-modules
            # not installable via pip, e.g., ["multi_tool_agent"] if it contained complex local packages.
            # For a simple structure where agent.py is directly in multi_tool_agent,
            # it's often handled by the SDK finding the root_agent import.
            # We can add 'multi_tool_agent' to extra_packages to be safe if direct import isn't enough for packaging.
            extra_packages=["multi_tool_agent"], 
            # env_vars can be used to set environment variables for the deployed agent
            # env_vars={"MY_CONFIG_VARIABLE": "my_value"},
        )
        print(f"Agent deployed successfully!")
        print(f"Resource Name: {remote_app.resource_name}")
        print(f"You can now interact with your agent using this resource name.")
        # The actual serving endpoint might be discoverable via other gcloud commands
        # or by constructing it based on the resource name, but the SDK itself
        # primarily gives the resource_name for management.
        # For ADK agents, interaction is typically via the SDK or specific API calls
        # using the session/agent resource name.

    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        print("Please check the following:")
        print("1. Ensure the GCS staging bucket exists and you have permissions.")
        print("2. Verify the agent code in 'multi_tool_agent/agent.py' and 'requirements_agent_engine.txt' are correct.")
        print("3. Check Vertex AI Agent Engine and ADK documentation for recent changes if errors persist.")

if __name__ == "__main__":
    deploy_agent() 