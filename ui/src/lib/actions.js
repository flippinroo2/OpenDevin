import {} from '$lib/store';

const messageActions = {
  initialize: () => {
    // store.dispatch(setInitialized(true));
    // store.dispatch(
    //   appendAssistantMessage(
    //     "Hi! I'm OpenDevin, an AI Software Engineer. What would you like to build with me today?",
    //   ),
    // );
  },
  browse: (message) => {
    const { url, screenshotSrc } = message.args;
    // store.dispatch(setUrl(url));
    // store.dispatch(setScreenshotSrc(screenshotSrc));
  },
  write: (message) => {
    // store.dispatch(setCode(message.args.content));
  },
  // "think" comes from an Observation
  think: (message) => {
    // store.dispatch(appendAssistantMessage(message.args.thought));
  },
  finish: (message) => {
    // store.dispatch(appendAssistantMessage(message.message));
  },
};

export function handleActionMessage(message) {
  if (message.action in messageActions) {
    const actionFn =
      messageActions[message.action];
    actionFn(message);
  }
}
