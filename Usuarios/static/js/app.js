navigator.serviceWorker.register("./static/js/service-worker.js").then(registration => {
    console.log("success!");
    if (registration.installing) {
      registration.installing.postMessage("Howdy from your installing page.");
    }
  }, err => {
    console.error("Installing the worker failed!", err);
  });