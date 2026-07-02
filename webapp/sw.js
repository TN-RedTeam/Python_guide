/* Service worker — Python Guide
   Stratégie simple et sûre :
   - coquille de l'app (HTML/CSS/JS/contenu) : réseau d'abord, cache en secours
     → l'app reste utilisable hors ligne après la première visite ;
   - CDN (CodeMirror, marked, Pyodide) : cache d'abord (ces URLs sont versionnées).
   NB : Pyodide pèse ~10 Mo ; il n'est mis en cache qu'après une première exécution. */

const VERSION = "pyguide-v1";
const APP_SHELL = [
  "./",
  "./index.html",
  "./css/style.css",
  "./js/app.js",
  "./content.json",
  "./manifest.webmanifest",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./vendor/marked.min.js",
  "./vendor/codemirror/codemirror.min.js",
  "./vendor/codemirror/codemirror.min.css",
  "./vendor/codemirror/python.min.js",
  "./vendor/codemirror/material-darker.min.css",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(VERSION).then((cache) => cache.addAll(APP_SHELL)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== "GET") return;

  if (url.origin === location.origin) {
    // App : réseau d'abord (toujours à jour), cache si hors ligne.
    event.respondWith(
      fetch(event.request)
        .then((rep) => {
          const copie = rep.clone();
          caches.open(VERSION).then((c) => c.put(event.request, copie));
          return rep;
        })
        .catch(() => caches.match(event.request, { ignoreSearch: true }))
    );
  } else if (/cdn\.jsdelivr\.net/.test(url.host)) {
    // CDN versionné : cache d'abord.
    event.respondWith(
      caches.match(event.request).then(
        (hit) => hit || fetch(event.request).then((rep) => {
          if (rep.ok) {
            const copie = rep.clone();
            caches.open(VERSION).then((c) => c.put(event.request, copie));
          }
          return rep;
        })
      )
    );
  }
});
