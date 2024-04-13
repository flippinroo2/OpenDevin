import json

import agenthub  # noqa F401 (we import this to get the agents registered)
import litellm
import tiktoken
from fastapi import FastAPI, Request, WebSocket, status
from fastapi.middleware.cors import CORSMiddleware
from flask import jsonify
from opendevin.agent import Agent
from opendevin.server.session import Session
from pydantic import BaseModel, Field
from src.config import Config, get_or_error
from src.logger import Logger, route_logger
from src.project import ProjectManager

config = Config()
logger = Logger()
manager = ProjectManager()

TIKTOKEN_ENC = tiktoken.get_encoding("cl100k_base")

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


@app.post(
    "/create-project", response_model=RequestData, status_code=status.HTTP_201_CREATED
)
# @route_logger(logger)
async def create_project(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    manager.create_project(project_name)
    return jsonify({"message": "Project created"})


@app.post(path="/calculate-tokens")
@route_logger(logger)
async def calculate_tokens(request: Request):
    json = await request.json()
    prompt = json.get("prompt")
    tokens = len(TIKTOKEN_ENC.encode(prompt))
    return jsonify({"token_usage": tokens})


@app.post("/delete-project")
async def delete_project(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/download-project")
async def download_project(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/download-project-pdf")
async def download_project_pdf(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
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
async def execute_agent(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/get-agent-state")
async def get_agent_state(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.post("/get-agent-state")
async def post_agent_state(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/browser-snapshot")
async def get_browser_snapshot(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/messages")
async def get_messages(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
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
async def get_logs(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")


@app.get("/settings")
async def get_settings(request: Request):
    json = await request.json()
    project_name = json.get("project_name")
    # manager.create_project(project_name)
    # return jsonify({"message": "Project created"})
    print("DEBUG")
