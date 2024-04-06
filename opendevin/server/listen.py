from typing import Any

import agenthub  # noqa F401 (we import this to get the agents registered)
import litellm
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from opendevin.agent import Agent
from opendevin.server.session import Session
from src.config import Config, get_or_error

config = Config()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{config.get_hostname()}:{config.get_port_number()}"],
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


@app.get("/default-model")
def read_default_model() -> str | Any:
    default_model: str | Any = get_or_error("LLM_MODEL")
    print(f"\n/default-model -> {default_model}\n")
    return default_model
