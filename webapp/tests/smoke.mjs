// Test de fumée de la plateforme e-learning (webapp/).
//
// Vérifie, dans un vrai navigateur (Chromium/Playwright), que l'app se charge,
// navigue et rend correctement — SANS exécuter Pyodide (on ne dépend d'aucun
// CDN, le test reste rapide et fiable en CI).
//
// Local :  NODE_PATH=/opt/node22/lib/node_modules \
//          PW_EXECUTABLE=/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
//          node webapp/tests/smoke.mjs
// CI    :  npx playwright install chromium  &&  node webapp/tests/smoke.mjs
//
// Le test sert lui-même webapp/ via `python3 -m http.server` puis l'arrête.

import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import path from "node:path";
import net from "node:net";

// `playwright` (installé dans ce dossier en CI) ; PW_REQUIRE permet de pointer
// une install globale en local (ex : /opt/node22/lib/node_modules/playwright).
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PW_REQUIRE || "playwright");

const WEBAPP = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PORT = 8977;
const BASE = `http://127.0.0.1:${PORT}`;

let failures = 0;
function ok(cond, label) {
  console.log(`${cond ? "✅" : "❌"} ${label}`);
  if (!cond) failures++;
}

function attendrePort(port, timeoutMs = 15000) {
  const t0 = Date.now();
  return new Promise((resolve, reject) => {
    const essai = () => {
      const s = net.connect(port, "127.0.0.1");
      s.on("connect", () => { s.destroy(); resolve(); });
      s.on("error", () => {
        s.destroy();
        if (Date.now() - t0 > timeoutMs) reject(new Error("serveur injoignable"));
        else setTimeout(essai, 200);
      });
    };
    essai();
  });
}

const serveur = spawn("python3", ["-m", "http.server", String(PORT)], {
  cwd: WEBAPP, stdio: "ignore",
});

(async () => {
  await attendrePort(PORT);
  const browser = await chromium.launch({
    executablePath: process.env.PW_EXECUTABLE || undefined,
    args: ["--no-sandbox", "--no-proxy-server"],
  });
  const page = await (await browser.newContext({
    viewport: { width: 412, height: 915 }, isMobile: true, hasTouch: true, serviceWorkers: "block",
  })).newPage();

  const erreurs = [];
  page.on("pageerror", (e) => erreurs.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error") erreurs.push("console: " + m.text()); });

  // 1. Accueil
  await page.goto(`${BASE}/index.html#/`, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".hero", { timeout: 15000 });
  ok((await page.locator(".cards .card").count()) >= 10, "Accueil : cartes du parcours");
  ok((await page.locator('.nav-item[data-route="module/penser_comme_un_dev"]').count()) === 1,
    "Menu : module fondation présent");

  // 2. Un module : cours + encadrés typés
  await page.goto(`${BASE}/index.html#/module/penser_comme_un_dev`, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".md", { timeout: 10000 });
  ok((await page.locator(".md .callout").count()) >= 3, "Module : encadrés typés rendus");
  ok((await page.locator(".tabs .tab").count()) >= 2, "Module : onglets présents");

  // 3. Onglet exercices : éditeur + terminal montés
  await page.click('.tab[data-tab="exercices"]');
  await page.waitForSelector(".CodeMirror", { timeout: 10000 });
  ok((await page.locator(".terminal-input").count()) === 1, "Exercices : terminal interactif monté");

  // 3bis. Quiz : questions rendues + correction fonctionnelle
  await page.click('.tab[data-tab="quiz"]');
  await page.waitForSelector(".quiz-q", { timeout: 10000 });
  const nbQ = await page.locator(".quiz-q").count();
  ok(nbQ >= 1, "Quiz : questions rendues");
  await page.click('.quiz-q[data-i="0"] .quiz-opt:first-child input');
  await page.click('[data-act="valider-quiz"]');
  await page.waitForSelector(".score-banner", { timeout: 5000 });
  ok((await page.locator(".quiz-expl:visible").count()) === nbQ, "Quiz : correction + explications affichées");

  // 4. Section pentest
  await page.goto(`${BASE}/index.html#/pentest`, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".tabs .tab", { timeout: 10000 });
  ok((await page.locator(".tabs .tab").count()) >= 7, "Pentest : onglets des groupes");

  // 5. Bac à sable
  await page.goto(`${BASE}/index.html#/ide`, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".CodeMirror", { timeout: 10000 });
  ok((await page.locator(".terminal-input").count()) === 1, "Bac à sable : éditeur + terminal");

  const fatales = erreurs.filter((e) => !/favicon|manifest|Failed to load resource|serviceWorker|sw\.js/.test(e));
  ok(fatales.length === 0, "Aucune erreur JS fatale" + (fatales.length ? " :\n   " + fatales.join("\n   ") : ""));

  await browser.close();
})()
  .catch((e) => { console.error("ÉCHEC:", e.message); failures++; })
  .finally(() => {
    serveur.kill();
    console.log(failures ? `\n❌ ${failures} test(s) en échec.` : "\n✅ Tous les tests de fumée passent.");
    process.exit(failures ? 1 : 0);
  });
