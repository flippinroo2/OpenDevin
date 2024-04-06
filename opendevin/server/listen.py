import json

import agenthub  # noqa F401 (we import this to get the agents registered)
import litellm
from fastapi import FastAPI, Request, WebSocket, status
from fastapi.middleware.cors import CORSMiddleware
from opendevin.agent import Agent
from opendevin.server.session import Session
from pydantic import BaseModel, Field
from src.config import Config, get_or_error

config = Config()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # f"http://{config.get_hostname()}:{config.get_port_number()-1}",
        # f"http://{config.get_hostname()}:{config.get_port_number()}",
        # f"http://{config.get_hostname()}:{config.get_port_number()+1}",
        "*"  # TODO: Set this up properly
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

litellm.set_verbose = True  # Setting verbose mode for Lite LLM


# This endpoint receives events from the client (i.e. the browser)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    session = Session(websocket)
    # TODO: should this use asyncio instead of await?
    await session.start_listening()


class RequestData(BaseModel):
    # project_name: str
    project_name: str = Field("")


@app.post("/create-project", status_code=status.HTTP_201_CREATED)
def create_project(request: Request, project_name: RequestData):
    print("DEBUG")


@app.post("/delete-project")
def delete_project(request: Request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/download-project")
def download_project(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/download-project-pdf")
def download_project_pdf(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/default-data")
def get_default_data() -> str:
    project_list = []
    model_list = [get_or_error("LLM_MODEL")]
    agent_list = []
    search_engine_list = []
    # return_value = {
    #     "project_list": project_list,
    #     "model_list": model_list,
    #     "agent_list": agent_list,
    #     "search_engine_list": search_engine_list,
    # }
    return_value: str = json.dumps(
        {
            "project_list": project_list,
            "model_list": model_list,
            "agent_list": agent_list,
            "search_engine_list": search_engine_list,
        }
    )
    return return_value


@app.get("/execute-agent")
def execute_agent(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/get-agent-state")
def get_agent_state(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/browser-snapshot")
def get_browser_snapshot(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/messages")
def get_messages(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/litellm-models")
async def get_litellm_models():
    """
    Get all models supported by LiteLLM.
    """
    return litellm.model_list


@app.get("/litellm-agents")
async def get_litellm_agents():
    """
    Get all agents supported by LiteLLM.
    """
    return Agent.listAgents()


@app.get("/logs")
def get_logs(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/settings")
def get_settings(request):
    data = request.json
    project_name = data.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")
