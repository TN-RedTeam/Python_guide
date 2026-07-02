/* ════════════════════════════════════════════════════════════════════
   Python Guide — plateforme e-learning interactive
   - Routage par hash (#/module/…, #/ide, …) : fonctionne en statique
   - Cours : markdown rendu par marked, liens internes réécrits
   - IDE : CodeMirror (édition) + Pyodide (vrai Python dans le navigateur)
   - Progression : localStorage (aucun serveur, aucune donnée envoyée)
   ════════════════════════════════════════════════════════════════════ */

"use strict";

const REPO_URL = "https://github.com/TN-RedTeam/Python_guide/blob/main/";
// Pyodide (le vrai Python compilé en WebAssembly) reste sur CDN : trop lourd
// pour être embarqué. `window.PYODIDE_BASE` permet de le servir ailleurs
// (miroir local, tests…).
const PYODIDE_URL = (window.PYODIDE_BASE || "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/") + "pyodide.js";

let CONTENT = null;          // content.json (modules, guides, projets)
let pyodideReady = null;     // promesse partagée : Pyodide ne se charge qu'une fois
let editors = {};            // instances CodeMirror de la vue courante

const $ = (sel, root = document) => root.querySelector(sel);
const view = $("#view");

/* ─────────────────────────── Stockage local ─────────────────────────── */

const store = {
  read(key, fallback) {
    try { return JSON.parse(localStorage.getItem("pyguide." + key)) ?? fallback; }
    catch { return fallback; }
  },
  write(key, value) {
    try { localStorage.setItem("pyguide." + key, JSON.stringify(value)); } catch { /* stockage plein/privé */ }
  },
};

const progress = {
  all: () => store.read("progress", {}),
  of: (id) => progress.all()[id] || {},
  update(id, patch) {
    const all = progress.all();
    all[id] = { ...(all[id] || {}), ...patch };
    store.write("progress", all);
    renderGlobalProgress();
  },
};

function moduleStatus(mod) {
  const p = progress.of(mod.id);
  if (p.total > 0 && p.ok === p.total) return "done";
  if (p.ok > 0 || p.visited) return "started";
  return "todo";
}

function globalPercent() {
  const mods = CONTENT.modules;
  let score = 0;
  for (const m of mods) {
    const p = progress.of(m.id);
    if (p.total > 0) score += Math.min(1, p.ok / p.total);
    else if (p.visited) score += 1;             // module sans exercices : lu = fait
  }
  return Math.round((score / mods.length) * 100);
}

function renderGlobalProgress() {
  if (!CONTENT) return;
  $("#global-progress").textContent = globalPercent() + " %";
}

/* ─────────────────────────── Thème ─────────────────────────── */

function applyTheme(theme) {
  document.body.dataset.theme = theme;
  $("#btn-theme").textContent = theme === "dark" ? "🌙" : "☀️";
  store.write("theme", theme);
  const meta = $('meta[name="theme-color"]');
  if (meta) meta.content = theme === "dark" ? "#0f1220" : "#f4f5fb";
}

$("#btn-theme").addEventListener("click", () =>
  applyTheme(document.body.dataset.theme === "dark" ? "light" : "dark"));

/* ─────────────────────────── Menu latéral ─────────────────────────── */

const sidebar = $("#sidebar");
const backdrop = $("#backdrop");

function toggleMenu(open) {
  sidebar.classList.toggle("open", open);
  backdrop.hidden = !open;
}
$("#btn-menu").addEventListener("click", () => toggleMenu(true));
$("#btn-close-menu").addEventListener("click", () => toggleMenu(false));
backdrop.addEventListener("click", () => toggleMenu(false));

function statusIcon(mod) {
  return { done: "✅", started: "🔵", todo: "" }[moduleStatus(mod)];
}

function buildNav() {
  const parts = [`<div class="nav-section">Parcours</div>`];
  for (const m of CONTENT.modules) {
    parts.push(`<a class="nav-item" data-route="module/${m.id}" href="#/module/${m.id}">
      <span>${m.emoji}</span> ${m.num} · ${escapeHtml(m.title)}
      <span class="st">${statusIcon(m)}</span></a>`);
  }
  parts.push(`<div class="nav-section">Pratiquer</div>`);
  parts.push(`<a class="nav-item" data-route="ide" href="#/ide"><span>⌨️</span> Bac à sable (IDE)</a>`);
  parts.push(`<a class="nav-item" data-route="projets" href="#/projets"><span>🧩</span> Mini-projets</a>`);
  parts.push(`<div class="nav-section">Guides</div>`);
  for (const g of CONTENT.guides) {
    parts.push(`<a class="nav-item" data-route="guide/${g.id}" href="#/guide/${g.id}">
      <span>${g.emoji}</span> ${escapeHtml(g.title)}</a>`);
  }
  $("#nav-list").innerHTML = parts.join("");
}

function highlightNav(route) {
  document.querySelectorAll(".nav-item").forEach((a) =>
    a.classList.toggle("active", a.dataset.route === route));
  const section = route.startsWith("module/") ? "cours"
    : route === "ide" ? "ide"
    : route.startsWith("guide") ? "guides"
    : route === "" ? "home" : "";
  document.querySelectorAll(".bottombar a").forEach((a) =>
    a.classList.toggle("active", a.dataset.nav === section));
}

/* ─────────────────────────── Markdown ─────────────────────────── */

function escapeHtml(s) {
  return s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function renderMarkdown(md, container) {
  container.innerHTML = marked.parse(md, { mangle: false, headerIds: false });

  // Tableaux : défilement horizontal sur mobile plutôt que déborder.
  container.querySelectorAll("table").forEach((t) => {
    const wrap = document.createElement("div");
    wrap.className = "table-wrap";
    t.replaceWith(wrap);
    wrap.appendChild(t);
  });

  // Liens internes du dépôt → routes de l'app ; le reste → GitHub.
  container.querySelectorAll("a[href]").forEach((a) => {
    const href = a.getAttribute("href");
    if (/^(https?:|mailto:|#)/.test(href)) {
      if (/^https?:/.test(href)) { a.target = "_blank"; a.rel = "noopener"; }
      return;
    }
    const clean = href.replace(/^(\.\/|\.\.\/)+/, "").replace(/\/$/, "").replace(/\/README\.md$/i, "");
    const mod = CONTENT.modules.find((m) => m.id === clean);
    const guide = CONTENT.guides.find((g) => g.id + ".md" === clean || g.id === clean);
    if (mod) a.setAttribute("href", `#/module/${mod.id}`);
    else if (guide) a.setAttribute("href", `#/guide/${guide.id}`);
    else if (/^projets/.test(clean)) a.setAttribute("href", "#/projets");
    else { a.setAttribute("href", REPO_URL + clean); a.target = "_blank"; a.rel = "noopener"; }
  });

  // Blocs de code Python : bouton « Essayer » qui envoie le code dans l'IDE.
  container.querySelectorAll("pre code").forEach((code) => {
    if (!/language-python/.test(code.className)) return;
    const btn = document.createElement("button");
    btn.className = "try-btn";
    btn.textContent = "▶ Essayer";
    btn.addEventListener("click", () => {
      sessionStorage.setItem("pyguide.handoff", code.textContent);
      location.hash = "#/ide";
    });
    code.parentElement.appendChild(btn);
  });
}

/* ─────────────────────────── Pyodide (Python) ─────────────────────────── */

// Petit code d'adaptation exécuté une fois : input() → boîte de dialogue du
// navigateur, et asyncio.run() rendu compatible avec la boucle du navigateur.
const PY_SETUP = `
import builtins, asyncio, js

def _input(message=""):
    if message:
        print(message, end="")
    reponse = js.window.prompt(str(message), "")
    reponse = "" if reponse is None else str(reponse)
    print(reponse)   # comme dans un terminal : la réponse reste visible
    return reponse
builtins.input = _input

_asyncio_run_origine = asyncio.run
def _asyncio_run_compat(coro, **kwargs):
    try:
        return _asyncio_run_origine(coro, **kwargs)
    except RuntimeError:
        # Navigateur : une boucle tourne déjà -> on y planifie la coroutine.
        return asyncio.ensure_future(coro)
asyncio.run = _asyncio_run_compat
`;

// Après l'exécution : attendre les tâches asyncio encore en vol (module 08).
const PY_DRAIN = `
import asyncio as _a
_pending = [t for t in _a.all_tasks() if t is not _a.current_task() and not t.done()]
if _pending:
    await _a.gather(*_pending, return_exceptions=True)
`;

function ensurePyodide(onStatus) {
  if (!pyodideReady) {
    onStatus("Téléchargement de Python (~10 Mo, une seule fois)…");
    pyodideReady = new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = PYODIDE_URL;
      s.onload = async () => {
        try {
          const py = await loadPyodide();
          await py.runPythonAsync(PY_SETUP);
          resolve(py);
        } catch (e) { reject(e); }
      };
      s.onerror = () => reject(new Error("Impossible de charger Pyodide (réseau ?)"));
      document.head.appendChild(s);
    });
    pyodideReady.catch(() => { pyodideReady = null; });
  }
  return pyodideReady;
}

async function runPython(code, ui) {
  const t0 = performance.now();
  ui.clear();
  ui.status("Préparation…");
  let py;
  try {
    py = await ensurePyodide(ui.status);
  } catch (e) {
    ui.print("❌ " + e.message, "err");
    ui.status("");
    return null;
  }
  ui.status("Exécution…");
  py.setStdout({ batched: (s) => ui.print(s) });
  py.setStderr({ batched: (s) => ui.print(s, "err") });

  // Espace de noms neuf à chaque exécution (comme relancer `python fichier.py`).
  const ns = py.globals.get("dict")();
  ns.set("__name__", "__main__");
  let output = null;
  try {
    await py.runPythonAsync(code, { globals: ns });
    await py.runPythonAsync(PY_DRAIN);
    output = ui.text();
  } catch (e) {
    ui.print(formatPyError(e), "err");
  } finally {
    ns.destroy();
    const dt = ((performance.now() - t0) / 1000).toFixed(1);
    ui.status(`Terminé en ${dt} s`);
  }
  return output;
}

function formatPyError(e) {
  // On ne garde que la partie utile de la traceback (pas les couches Pyodide).
  const msg = String(e.message || e);
  const idx = msg.lastIndexOf('File "<exec>"');
  return idx >= 0 ? "❌ Erreur Python :\n" + msg.slice(idx) : "❌ " + msg;
}

/* ─────────────────────────── Composant IDE ─────────────────────────── */

function createIDE(host, options) {
  // options : { code, storageKey, note, onScore, extraButtons }
  const noteHtml = options.note
    ? `<div class="ide-note">💡 <div>${escapeHtml(options.note)}</div></div>` : "";
  host.innerHTML = `
    ${noteHtml}
    <div class="ide-toolbar">
      <button class="btn btn-primary" data-act="run">▶ Exécuter</button>
      ${(options.extraButtons || []).map((b, i) =>
        `<button class="btn btn-ghost" data-extra="${i}">${b.label}</button>`).join("")}
      <button class="btn btn-ghost" data-act="reset" title="Revenir au code d'origine">↺</button>
      <span class="spacer"></span>
      <span class="ide-status"></span>
    </div>
    <div class="editor-wrap"><textarea></textarea></div>
    <div class="score-slot"></div>
    <div class="console"><span class="sys">La sortie de ton programme s'affichera ici. Appuie sur ▶ Exécuter.</span></div>`;

  const saved = options.storageKey ? store.read("code." + options.storageKey, null) : null;
  const cm = CodeMirror.fromTextArea($("textarea", host), {
    mode: "python",
    theme: document.body.dataset.theme === "dark" ? "material-darker" : "default",
    lineNumbers: true,
    indentUnit: 4,
    viewportMargin: 50,
    inputStyle: "contenteditable",   // meilleur support des claviers Android
  });
  cm.setValue(saved ?? options.code ?? "");

  let saveTimer = null;
  cm.on("change", () => {
    if (!options.storageKey) return;
    clearTimeout(saveTimer);
    saveTimer = setTimeout(() => store.write("code." + options.storageKey, cm.getValue()), 400);
  });

  const consoleEl = $(".console", host);
  const statusEl = $(".ide-status", host);
  const ui = {
    clear: () => { consoleEl.textContent = ""; },
    print(s, cls) {
      const span = document.createElement("span");
      if (cls) span.className = cls;
      span.textContent = s + "\n";
      consoleEl.appendChild(span);
      consoleEl.scrollTop = consoleEl.scrollHeight;
    },
    text: () => consoleEl.textContent,
    status: (s) => { statusEl.textContent = s; },
  };

  const runBtn = $('[data-act="run"]', host);
  runBtn.addEventListener("click", async () => {
    runBtn.disabled = true;
    const output = await runPython(cm.getValue(), ui);
    runBtn.disabled = false;
    if (output !== null && options.onScore) {
      const m = output.match(/(\d+)\s*\/\s*(\d+)\s+réussis/);
      if (m) options.onScore(Number(m[1]), Number(m[2]), host);
    }
  });

  $('[data-act="reset"]', host).addEventListener("click", () => {
    if (confirm("Revenir au code d'origine ? Tes modifications ici seront effacées.")) {
      cm.setValue(options.code ?? "");
    }
  });

  (options.extraButtons || []).forEach((b, i) =>
    $(`[data-extra="${i}"]`, host).addEventListener("click", () => b.onClick(cm, host)));

  editors[options.storageKey || "tmp"] = cm;
  setTimeout(() => cm.refresh(), 0);
  return cm;
}

function showScore(ok, total, host) {
  const slot = $(".score-slot", host);
  const win = ok === total;
  slot.innerHTML = `<div class="score-banner ${win ? "win" : "partial"}">
    ${win ? "🎉 Bravo, " : "💪 Continue : "} ${ok}/${total} exercices réussis${win ? " !" : "."}
  </div>`;
}

/* ─────────────────────────── Vues ─────────────────────────── */

function viewHome() {
  const pct = globalPercent();
  const lastId = store.read("lastModule", null);
  const last = CONTENT.modules.find((m) => m.id === lastId);
  const cont = last
    ? `<a class="btn btn-light" href="#/module/${last.id}">▶ Continuer : ${last.num} · ${escapeHtml(last.title)}</a>`
    : `<a class="btn btn-light" href="#/module/00_demarrer">▶ Commencer le parcours</a>`;

  const cards = CONTENT.modules.map((m) => {
    const p = progress.of(m.id);
    const sub = p.total > 0 ? `Exercices : ${p.ok}/${p.total} réussis`
      : m.exercices ? "Exercices auto-corrigés" : "Lecture + démos";
    return `<a class="card" href="#/module/${m.id}">
      <span class="emoji">${m.emoji}</span>
      <span class="card-body">
        <div class="card-title">${m.num} · ${escapeHtml(m.title)}</div>
        <div class="card-sub">${sub}</div>
      </span>
      <span class="badge">${statusIcon(m)}</span></a>`;
  }).join("");

  const guides = CONTENT.guides.map((g) =>
    `<a class="card" href="#/guide/${g.id}"><span class="emoji">${g.emoji}</span>
      <span class="card-body"><div class="card-title">${escapeHtml(g.title)}</div></span></a>`).join("");

  view.innerHTML = `
    <div class="hero">
      <h1>Apprends Python,<br>directement dans ton navigateur 🐍</h1>
      <p>Cours en français, exercices auto-corrigés et un vrai Python intégré —
         aucune installation, même sur ton téléphone Android.</p>
      ${cont}
      <div class="progress-track" style="margin-top:1rem"><div class="progress-fill" style="width:${pct}%"></div></div>
      <div class="progress-label">${pct} % du parcours complété</div>
    </div>

    <div class="section-title">🗺️ Le parcours (16 modules)</div>
    <div class="cards">${cards}</div>

    <div class="section-title">🛠️ Pratiquer</div>
    <div class="cards">
      <a class="card" href="#/ide"><span class="emoji">⌨️</span>
        <span class="card-body"><div class="card-title">Bac à sable</div>
        <div class="card-sub">Un IDE Python libre, pour tester ce que tu veux</div></span></a>
      <a class="card" href="#/projets"><span class="emoji">🧩</span>
        <span class="card-body"><div class="card-title">Mini-projets</div>
        <div class="card-sub">To-do list, carnet de contacts, générateur de mots de passe…</div></span></a>
    </div>

    <div class="section-title">🧭 Guides de survie</div>
    <div class="cards">${guides}</div>`;
}

function moduleTabs(mod, active) {
  const tabs = [["cours", "📖 Cours"]];
  if (mod.exercices) tabs.push(["exercices", "🧪 Exercices"]);
  if (mod.demos.length) tabs.push(["demo", "💻 Code du module"]);
  return `<div class="tabs">${tabs.map(([id, label]) =>
    `<button class="tab ${id === active ? "active" : ""}" data-tab="${id}">${label}</button>`).join("")}</div>`;
}

function viewModule(id, tab) {
  const mod = CONTENT.modules.find((m) => m.id === id);
  if (!mod) { location.hash = "#/"; return; }
  if (!tab) tab = "cours";
  progress.update(id, { visited: true });
  store.write("lastModule", id);
  buildNav(); // met à jour les pastilles de statut

  const idx = CONTENT.modules.indexOf(mod);
  const prev = CONTENT.modules[idx - 1];
  const next = CONTENT.modules[idx + 1];

  view.innerHTML = `
    <div class="module-head">
      <div class="crumbs"><a href="#/">Accueil</a> / Module ${mod.num}</div>
      <h1>${mod.emoji} ${escapeHtml(mod.title)}</h1>
    </div>
    ${moduleTabs(mod, tab)}
    <div id="tab-content"></div>
    <div class="pager">
      ${prev ? `<a class="btn btn-ghost" href="#/module/${prev.id}">← ${prev.num}</a>` : "<span></span>"}
      ${next ? `<a class="btn btn-primary" href="#/module/${next.id}">Module ${next.num} →</a>`
             : `<a class="btn btn-primary" href="#/projets">Les mini-projets →</a>`}
    </div>`;

  document.querySelectorAll(".tab").forEach((b) =>
    b.addEventListener("click", () => { location.hash = `#/module/${id}/${b.dataset.tab}`; }));

  const host = $("#tab-content");
  if (tab === "cours") {
    const md = document.createElement("div");
    md.className = "md";
    host.appendChild(md);
    renderMarkdown(mod.readme, md);
  } else if (tab === "exercices") {
    const note = mod.note || "Complète les fonctions (remplace les « ... »), puis ▶ Exécuter : "
      + "tu verras tes ✅/❌ en direct. Ton code est sauvegardé sur cet appareil.";
    createIDE(host, {
      code: mod.exercices,
      storageKey: id + ":exo",
      note,
      onScore: (ok, total, h) => {
        showScore(ok, total, h);
        progress.update(id, { ok, total });
        buildNav();
      },
      extraButtons: mod.solutions ? [{
        label: "👀 Solution",
        onClick: (cm, h) => toggleSolution(mod, h),
      }] : [],
    });
  } else if (tab === "demo") {
    host.innerHTML = `<div class="file-pills">${mod.demos.map((d, i) =>
      `<button class="file-pill ${i === 0 ? "active" : ""}" data-i="${i}">${d.name}</button>`).join("")}</div>
      <div id="demo-ide"></div>`;
    const loadDemo = (i) => {
      document.querySelectorAll(".file-pill").forEach((p, j) => p.classList.toggle("active", i === j));
      createIDE($("#demo-ide"), {
        code: mod.demos[i].code,
        storageKey: id + ":demo:" + mod.demos[i].name,
        note: mod.note,
      });
    };
    document.querySelectorAll(".file-pill").forEach((p) =>
      p.addEventListener("click", () => loadDemo(Number(p.dataset.i))));
    loadDemo(0);
  }
}

function toggleSolution(mod, host) {
  let box = $(".solution-box", host);
  if (box) { box.remove(); return; }
  box = document.createElement("div");
  box.className = "solution-box md";
  box.innerHTML = `<div class="ide-note">⚠️ <div>Le corrigé n'aide que si tu as vraiment essayé
    d'abord. Compare-le à TA version : l'écart entre les deux, c'est ta leçon.</div></div>
    <pre><code>${escapeHtml(mod.solutions)}</code></pre>`;
  $(".score-slot", host).before(box);
}

function viewGuides() {
  view.innerHTML = `
    <div class="module-head"><h1>🧭 Guides de survie</h1>
    <p style="color:var(--text-dim)">Les références à garder sous la main quand tu lis ou écris du code.</p></div>
    <div class="cards">${CONTENT.guides.map((g) =>
      `<a class="card" href="#/guide/${g.id}"><span class="emoji">${g.emoji}</span>
       <span class="card-body"><div class="card-title">${escapeHtml(g.title)}</div></span></a>`).join("")}</div>`;
}

function viewGuide(id) {
  const g = CONTENT.guides.find((x) => x.id === id);
  if (!g) { location.hash = "#/guides"; return; }
  view.innerHTML = `
    <div class="module-head">
      <div class="crumbs"><a href="#/">Accueil</a> / <a href="#/guides">Guides</a></div>
    </div><div class="md" id="guide-md"></div>`;
  renderMarkdown(g.md, $("#guide-md"));
}

function viewProjets(sub) {
  const pj = CONTENT.projets;
  const files = sub === "fil_rouge" ? pj.fil_rouge.files : pj.files;
  const readme = sub === "fil_rouge" ? pj.fil_rouge.readme : pj.readme;
  view.innerHTML = `
    <div class="module-head">
      <div class="crumbs"><a href="#/">Accueil</a> / Mini-projets</div>
    </div>
    <div class="tabs">
      <button class="tab ${sub !== "fil_rouge" ? "active" : ""}" data-go="#/projets">🧩 Mini-projets</button>
      <button class="tab ${sub === "fil_rouge" ? "active" : ""}" data-go="#/projets/fil_rouge">🧵 Projet fil rouge</button>
    </div>
    <div class="md" id="pj-md"></div>
    <div class="section-title">💻 Ouvrir le code</div>
    <div class="file-pills">${files.map((f, i) =>
      `<button class="file-pill" data-i="${i}">${f.name}</button>`).join("")}</div>
    <div id="pj-ide"></div>`;
  renderMarkdown(readme, $("#pj-md"));
  document.querySelectorAll(".tab").forEach((b) =>
    b.addEventListener("click", () => { location.hash = b.dataset.go; }));
  document.querySelectorAll(".file-pill").forEach((p) =>
    p.addEventListener("click", () => {
      document.querySelectorAll(".file-pill").forEach((x) => x.classList.remove("active"));
      p.classList.add("active");
      const f = files[Number(p.dataset.i)];
      createIDE($("#pj-ide"), {
        code: f.code,
        storageKey: "projets:" + (sub || "") + f.name,
        note: "Certains projets utilisent input() : le navigateur ouvrira une boîte de dialogue. "
            + "Ceux qui touchent au réseau ou aux vrais dossiers sont à lancer sur ta machine.",
      });
    }));
}

const IDE_DEFAULT = `# ⌨️ Bac à sable — écris du Python, appuie sur ▶ Exécuter.
# Tout tourne DANS ton navigateur : tu ne peux rien casser. Amuse-toi !

prenom = input("Comment tu t'appelles ? ")
print(f"Salut {prenom} ! 🐍")

for i in range(3, 0, -1):
    print(i, "…")
print("Décollage 🚀")
`;

function viewIDE() {
  view.innerHTML = `
    <div class="module-head"><h1>⌨️ Bac à sable</h1>
    <p style="color:var(--text-dim)">Un vrai Python (3.12) tourne dans ton navigateur grâce à
    <a href="https://pyodide.org" target="_blank" rel="noopener">Pyodide</a>.
    Premier lancement : ~10 Mo à télécharger, ensuite c'est instantané.</p></div>
    <div id="sandbox"></div>`;
  const handoff = sessionStorage.getItem("pyguide.handoff");
  if (handoff) {
    sessionStorage.removeItem("pyguide.handoff");
    store.write("code.sandbox", handoff);
  }
  createIDE($("#sandbox"), { code: IDE_DEFAULT, storageKey: "sandbox" });
}

/* ─────────────────────────── Routeur ─────────────────────────── */

function router() {
  toggleMenu(false);
  editors = {};
  const hash = location.hash.replace(/^#\/?/, "");
  const [root, a, b] = hash.split("/");
  window.scrollTo(0, 0);

  if (root === "module" && a) { viewModule(a, b); highlightNav("module/" + a); }
  else if (root === "guide" && a) { viewGuide(a); highlightNav("guide/" + a); }
  else if (root === "guides") { viewGuides(); highlightNav("guides"); }
  else if (root === "projets") { viewProjets(a); highlightNav("projets"); }
  else if (root === "ide") { viewIDE(); highlightNav("ide"); }
  else { viewHome(); highlightNav(""); }
}

/* ─────────────────────────── Démarrage ─────────────────────────── */

async function boot() {
  applyTheme(store.read("theme", "dark"));
  try {
    const rep = await fetch("content.json");
    CONTENT = await rep.json();
  } catch {
    view.innerHTML = `<div class="loading-screen"><p>❌ Impossible de charger les cours
      (content.json). Si tu lances le site en local, sers-le avec :<br>
      <code>python3 -m http.server</code> depuis le dossier webapp/.</p></div>`;
    return;
  }
  buildNav();
  renderGlobalProgress();
  window.addEventListener("hashchange", router);
  router();

  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("sw.js").catch(() => { /* hors ligne indisponible, pas bloquant */ });
  }
}

boot();
