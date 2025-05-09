FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY multi_tool_agent/ ./multi_tool_agent/
COPY multi_tool_agent/.env ./multi_tool_agent/.env

# Assuming your agent is started by running the agent.py script.
# If you have a different way to start it (e.g., a main.py that imports and runs the agent),
# please adjust the CMD instruction.
# For Cloud Run, your application needs to listen on the port defined by the PORT environment variable.
# The google-adk Agent might handle this automatically or require specific configuration.
# For now, I'll assume a simple execution. If it needs to be served via an HTTP server,
# we might need to add gunicorn or a similar WSGI server.
CMD ["python", "multi_tool_agent/agent.py"] 