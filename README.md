# Deploying Google ADK Agent to Cloud Run

A checklist and project plan for developing and deploying a Google Agent Development Kit (ADK) agent as a containerized service on Google Cloud Run.

## Project Status Legend
- [ ] Not Started
- [x] In Progress (if you want to mark something as started)
- [X] Complete (Note: Markdown might render this as a checked box or just with an X)

## 1. Google Cloud Setup
- [ ] Google Cloud Project selected/created.
- [ ] Required APIs enabled:
    - [ ] Vertex AI API
    - [ ] Cloud Run API
    - [ ] Secret Manager API
    - [ ] Artifact Registry API
    - [ ] IAM API
- [ ] `gcloud` CLI installed and configured for the correct project.

## 2. Agent Development & Configuration
- [X] Google ADK and `python-dotenv` added to `requirements.txt`.
- [X] Agent logic developed in `multi_tool_agent/agent.py` (with `root_agent` variable).
- [X] Agent configured in `multi_tool_agent/agent.py` to load `.env` file using `python-dotenv`.
- [ ] Identify all environment variables required by the agent.
- [X] **Crucial:** ADK Agent serving mechanism for Cloud Run determined:
    - [X] Will use FastAPI and Uvicorn with a custom `main.py` as per ADK documentation for `gcloud run deploy`.
    - [ ] Create `main.py` in the project root to initialize the FastAPI app using `google.adk.cli.fast_api.get_fast_api_app()` and run it with `uvicorn`.
    - [X] Ensure `multi_tool_agent/__init__.py` is set up (e.g., `from . import agent` or `from .agent import root_agent`) so `main.py` can load the agent.
- [X] Add `fastapi` and `uvicorn[standard]` to `requirements.txt`.
- [X] Agent tested locally by running `python main.py` (or `uvicorn main:app --reload`) and sending HTTP requests.
- [X] Local testing confirms interaction with any necessary services (e.g., Vertex AI if configured).

## 3. Environment & Secret Management
- [X] `.env` file (`multi_tool_agent/.env`) will be used for environment variables loaded by `python-dotenv`.
- [ ] **Security Review**:
    - [ ] Identify sensitive variables in `multi_tool_agent/.env` (e.g., API keys, credentials).
    - [ ] Plan to store all sensitive variables as secrets in Google Secret Manager.
    - [ ] Identify non-sensitive configuration variables (can be passed directly as env vars in Cloud Run).
- [ ] Store identified sensitive variables in Google Secret Manager.

## 4. Service Account & IAM Permissions
- [ ] Dedicated user-managed service account created for the Cloud Run service.
- [ ] Service account granted `Vertex AI User` role (`roles/aiplatform.user`).
- [ ] Service account granted `Secret Manager Secret Accessor` role (`roles/secretmanager.secretAccessor`) on the required secrets.
- [ ] Service account granted any other roles needed (e.g., for other Google Cloud services).

## 5. Containerization
- [X] `requirements.txt` created (to be updated with FastAPI/Uvicorn).
- [X] `Dockerfile` created:
    - [X] Uses `python:3.9-slim` base image (consider aligning with ADK docs `python:3.13-slim` and user creation).
    - [X] Sets `WORKDIR /app`.
    - [X] Copies `requirements.txt` and runs `pip install`.
    - [X] Copies the `multi_tool_agent/` directory into the image.
    - [X] Copies `multi_tool_agent/.env` into `/app/multi_tool_agent/.env` in the image.
    - [X] Copy `main.py` to `/app/main.py` in the `Dockerfile`.
    - [X] **Update `Dockerfile CMD`**: Set to `CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]`.
- [X] `.gitignore` file created/updated to include:
    - [X] `multi_tool_agent/.env`
    - [X] `.venv/`
    - [X] `__pycache__/`
    - [X] `*.pyc`
- [X] Docker image built locally (e.g., `docker build -t my-agent-app .`).
- [ ] Local Docker container tested:
    - [x] Run with port mapping and environment variables: `docker run -p 8080:8080 -e PORT=8080 --env-file multi_tool_agent/.env my-agent-app`.
    - [x] Test by sending HTTP requests to `http://localhost:8080`.
- [ ] Docker image pushed to Google Artifact Registry (e.g., `gcloud artifacts docker push ...`).

## 6. Cloud Run Deployment
- [ ] Cloud Run service name decided.
- [ ] `gcloud run deploy <SERVICE_NAME> --image <IMAGE_URL_FROM_ARTIFACT_REGISTRY>` command formulated, including:
    - [ ] `--region <REGION>`
    - [ ] `--platform managed`
    - [ ] `--service-account <YOUR_DEDICATED_SERVICE_ACCOUNT_EMAIL>`
    - [ ] `--set-secrets=ENV_VAR_NAME=secretName:version,...` for secrets from Secret Manager.
    - [ ] `--set-env-vars=ENV_VAR_NAME=value,...` for non-sensitive variables.
    - [ ] `--port 8080` (or the port your application listens on, matching `${PORT}`).
    - [ ] `--no-allow-unauthenticated` (recommended for private services).
    - [ ] (Optional) Resource allocation: `--cpu`, `--memory`.
    - [ ] (Optional) Scaling settings: `--min-instances`, `--max-instances`.
- [ ] Agent deployed to Cloud Run using the formulated `gcloud` command.
- [ ] Deployed service URL noted.
- [ ] Cloud Run logs monitored for initial deployment success and any startup issues.

## 7. Client Interaction & Authentication (Post-Deployment)
- [ ] Identity of the calling client/service determined (e.g., another service account, end-user).
- [ ] Calling identity granted the `Cloud Run Invoker` role (`roles/run.invoker`) on the deployed Cloud Run service.
- [ ] Client application/script developed/updated to:
    - [ ] Obtain a Google-signed ID token for the calling identity.
    - [ ] Include the ID token in the `Authorization: Bearer <ID_TOKEN>` header.
    - [ ] Send requests to the Cloud Run service URL with the expected ADK agent API payload.
    - [ ] Handle the response from the agent.
- [ ] Programmatic interaction tested from the client.
- [ ] Cloud Run logs monitored during client interaction.

## Security & Development Best Practices
- **Principle of Least Privilege**: Always use a dedicated service account for Cloud Run and grant only minimum necessary permissions.
- **Secret Management**: Avoid hardcoding secrets. Use Google Secret Manager and reference secrets in Cloud Run.
- **Private Services**: Default to `--no-allow-unauthenticated` for Cloud Run services.
- **Code Security**: Ensure input validation and safe handling in agent code.
- **Local Development**:
    - Use `.gitignore` for sensitive files (`.env`) and local artifacts (`.venv`, `__pycache__`).
    - (Optional) Use `gcloud auth application-default login` for local Google Cloud authentication.

This checklist should provide a good roadmap. The next key steps involve implementing the `main.py` for FastAPI/Uvicorn, updating `requirements.txt`, and adjusting the `Dockerfile` accordingly. 