import {
  agentState,
  internet,
  modelList,
  projectList,
  messages,
  searchEngineList,
} from "./store";
// import { io } from "socket.io-client";

const PORT = 3000;
// const PORT = 1337;

const getApiBaseUrl = () => {
  if (typeof window !== 'undefined') {
    // Client-side code
    const host = window.location.hostname;
    if (host === 'localhost' || host === '127.0.0.1') {
      return `http://127.0.0.1:${PORT}`;
    } else {
      return `http://${host}:${PORT}`;
    }
  } else {
    // Server-side code (Node.js)
    return `http://127.0.0.1:${PORT}`;
  }
};

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || getApiBaseUrl();
// export const socket = io(API_BASE_URL);


const WS_URL = `ws://localhost:3000/ws`;
// export const socket = new WebSocket(WS_URL);
export const socket = {}


export async function fetchInitialData() {
  const response = await fetch(`${API_BASE_URL}/default-data`);
  const data = JSON.parse(await response.json());
  projectList.set(data.projects);
  modelList.set(data.models);
  searchEngineList.set(data.search_engines);
  localStorage.setItem("defaultData", JSON.stringify(data));
}

export async function createProject(projectName) {
  const request_body = JSON.stringify({ project_name: projectName })
  await fetch(`${API_BASE_URL}/create-project`, {
    method: "POST",
    body: request_body,
  });
  projectList.update((projects) => [...projects, projectName]);
}

export async function deleteProject(projectName) {
  await fetch(`${API_BASE_URL}/delete-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
}

export async function fetchMessages() {
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  messages.set(data.messages);
}

export async function fetchAgentState() {
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/get-agent-state`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  agentState.set(data.state);
}

export async function executeAgent(prompt) {
  const projectName = localStorage.getItem("selectedProject");
  const modelId = localStorage.getItem("selectedModel");

  if (!modelId) {
    alert("Please select the LLM model first.");
    return;
  }

  await fetch(`${API_BASE_URL}/execute-agent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt: prompt,
      base_model: modelId,
      project_name: projectName,
    }),
  });

  await fetchMessages();
}

export async function getBrowserSnapshot(snapshotPath) {
  const response = await fetch(`${API_BASE_URL}/browser-snapshot`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ snapshot_path: snapshotPath }),
  });
  const data = await response.json();
  return data.snapshot;
}

export async function checkInternetStatus() {
  if (navigator.onLine) {
    internet.set(true);
  } else {
    internet.set(false);
  }
}

export async function fetchSettings() {
  const response = await fetch(`${API_BASE_URL}/settings`);
  const data = await response.json();
  return data.settings;
}

export async function updateSettings(settings) {
  await fetch(`${API_BASE_URL}/settings`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(settings),
  });
}

export async function fetchLogs() {
  const response = await fetch(`${API_BASE_URL}/logs`);
  const data = await response.json();
  return data.logs;
}
