# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the agent code into the container
COPY multi_tool_agent/ ./multi_tool_agent/

# Copy the main application file
COPY main.py main.py

# Copy the .env file for the agent (if it's not exclusively for local dev and needed in the container)
# Ensure this is appropriate for your security model. Secrets are better handled via Secret Manager in Cloud Run.
COPY multi_tool_agent/.env ./multi_tool_agent/.env

# Make port 8080 available to the world outside this container
# Cloud Run will set the PORT environment variable, Uvicorn will use it.
EXPOSE 8080

# Define environment variable for the PORT (Uvicorn will pick this up if set)
# ENV PORT 8080 # This is often set by the Cloud Run environment itself.

# Run main.py when the container launches
# The command uses sh -c to properly expand the $PORT environment variable.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"] 