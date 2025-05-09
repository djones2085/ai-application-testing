'''Main application file to run the ADK Agent using FastAPI and Uvicorn.
'''
import os
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

# The agent is expected to be in a subdirectory, conventionally `multi_tool_agent`,
# relative to the location of this main.py file.
# The ADK tools will discover the agent (e.g., root_agent in multi_tool_agent.agent)
# based on the agent_dir.

# Get the directory where main.py is located (project root)
AGENT_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Default session database URL (SQLite in the current directory)
# You might want to configure this differently for production.
DEFAULT_SESSION_DB_URL = f"sqlite:///./sessions.db"
SESSION_DB_URL = os.environ.get("SESSION_DB_URL", DEFAULT_SESSION_DB_URL)

# Allowed origins for CORS. Adjust for production.
# For local development, "*" is often used but is insecure for production.
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "http://localhost,http://localhost:8080,*").split(",")

# Initialize the FastAPI app with the ADK agent
# web=True enables the ADK's built-in development UI (handy for testing)
app: FastAPI = get_fast_api_app(
    agent_dir=AGENT_PROJECT_ROOT, # Points to the directory containing 'multi_tool_agent'
    session_db_url=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
    web=True # Enable ADK dev UI, can be configured via env var if needed
)

if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # Run the Uvicorn server
    # Host "0.0.0.0" makes the server accessible externally (e.g., within a Docker container)
    uvicorn.run(app, host="0.0.0.0", port=port) 