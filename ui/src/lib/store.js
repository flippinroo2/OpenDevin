import { writable } from 'svelte/store';

const getInitialSelectedProject = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedProject') || '';
  }
  return '';
};

const getInitialSelectedModel = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedModel') || '';
  }
  return '';
};

const getInitialSelectedAgent = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedAgent') || '';
  }
  return '';
};

const getInitialSelectedSearchEngine = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedSearchEngine') || '';
  }
  return '';
};

export const projectList = writable([]);
export const selectedProject = writable(getInitialSelectedProject());

export const modelList = writable({});
export const selectedModel = writable(getInitialSelectedModel());

export const agentList = writable({});
export const selectedAgent = writable(getInitialSelectedAgent());

export const searchEngineList = writable([]);
export const selectedSearchEngine = writable(getInitialSelectedSearchEngine());

export const agentState = writable(null);

export const isInitialized = writable(false);
export const isComplete = writable(false);

export const thoughts = writable([]);
export const messages = writable([]);

export const code = writable("");
export const internet = writable(true);
export const tokenUsage = writable(0);

selectedProject.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedProject', value);
  }
});

selectedModel.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedModel', value);
  }
});

selectedAgent.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedAgent', value);
  }
});

selectedSearchEngine.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedSearchEngine', value);
  }
});