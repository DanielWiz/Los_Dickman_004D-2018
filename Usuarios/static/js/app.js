if ('serviceWorker' in navigator) {
    navigator.serviceWorker
             .register('./static/js/service-worker.js')
             .then(function() { console.log('Service Worker Registered'); });
  }
