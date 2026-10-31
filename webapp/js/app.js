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
      <span>${m.emoji}</span> ${m.num ? m.num + " · " : ""}${escapeHtml(m.title)}
      <span class="st">${statusIcon(m)}</span></a>`);
  }
  parts.push(`<div class="nav-section">Pratiquer</div>`);
  parts.push(`<a class="nav-item" data-route="ide" href="#/ide"><span>⌨️</span> Bac à sable (IDE)</a>`);
  parts.push(`<a class="nav-item" data-route="projets" href="#/projets"><span>🧩</span> Mini-projets</a>`);
  parts.push(`<a class="nav-item" data-route="pentest" href="#/pentest"><span>🛡️</span> Pentest &amp; sécurité</a>`);
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

// Encadrés riches pour les cours : `:::type Titre` … `:::`. Le corps reste du
// markdown normal (marked le rend car les balises <div> sont séparées par des
// lignes vides). Types : objectif, idee, piege, astuce, etape, exemple, defi…
function preprocessMarkdown(md) {
  return md.replace(
    /^:::([a-zA-Zéè]+)(?:[ \t]+(.+?))?[ \t]*\n([\s\S]*?)\n:::[ \t]*$/gim,
    (_, type, titre, corps) => {
      const t = normaliserType(type);
      const tete = titre ? `<p class="callout-titre">${escapeHtml(titre.trim())}</p>\n\n` : "";
      return `\n<div class="callout callout-${t} callout-block">\n\n${tete}${corps.trim()}\n\n</div>\n`;
    }
  );
}

// Type d'encadré (français ou anglais) → classe CSS canonique.
function normaliserType(mot) {
  const map = {
    objectif: "goal", but: "goal", goal: "goal",
    idee: "idea", idée: "idea", cle: "idea", idea: "idea",
    piege: "warn", piège: "warn", attention: "warn", warn: "warn",
    astuce: "tip", tip: "tip", note: "note",
    danger: "danger", erreur: "danger",
    etape: "step", étape: "step", steps: "step",
    reflexion: "think", réflexion: "think", reflechis: "think", réfléchis: "think", think: "think",
    exemple: "example", example: "example",
    defi: "try", défi: "try", atoi: "try", try: "try", exo: "try",
    reussi: "success", ok: "success", success: "success",
  };
  return map[mot.toLowerCase()] || "note";
}

// Classe automatiquement les citations `> 🎯 …` existantes en encadrés typés,
// d'après l'emoji de tête — sans toucher au contenu des cours.
const EMOJI_CALLOUTS = [
  ["🎯", "goal"], ["🧠", "idea"], ["💡", "tip"], ["🔎", "tip"], ["🔍", "tip"],
  ["⚠️", "warn"], ["⚠", "warn"], ["❌", "danger"], ["🚫", "danger"], ["🛑", "danger"],
  ["✅", "success"], ["🎉", "success"], ["📝", "note"], ["📌", "note"], ["ℹ️", "note"],
  ["🧪", "try"], ["👉", "try"], ["✍️", "try"], ["🔢", "step"], ["🧩", "step"],
  ["🧭", "think"],
];

function enhanceMarkdown(container) {
  // Citations emoji → encadrés colorés (le contenu porte déjà l'emoji).
  container.querySelectorAll("blockquote").forEach((bq) => {
    if (bq.closest(".callout")) return;
    const txt = bq.textContent.trimStart();
    let type = "note";
    for (const [emoji, t] of EMOJI_CALLOUTS) {
      if (txt.startsWith(emoji)) { type = t; break; }
    }
    bq.classList.add("callout", "callout-" + type);
  });
}

function renderMarkdown(md, container) {
  container.innerHTML = marked.parse(preprocessMarkdown(md), { mangle: false, headerIds: false });
  enhanceMarkdown(container);

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

  // Blocs de code : « Essayer » (Python) et étiquette « Pseudo-code ».
  container.querySelectorAll("pre code").forEach((code) => {
    if (/language-(pseudo|texte|text)/.test(code.className)) {
      code.parentElement.classList.add("pseudo");
      return;
    }
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

# Terminal interactif : exécute une saisie dans l'espace de noms donné. Le mode
# "single" reproduit le vrai shell Python -> une expression seule affiche son
# résultat (repr) automatiquement, exactement comme dans « python » sur la ligne
# de commande. Plusieurs instructions collées -> on retombe sur "exec".
def _pyguide_terminal(saisie, espace):
    try:
        objet = compile(saisie, "<terminal>", "single")
    except SyntaxError:
        objet = compile(saisie, "<terminal>", "exec")
    exec(objet, espace)
`;

// Après l'exécution : attendre les tâches asyncio encore en vol (module 08).
const PY_DRAIN = `
import asyncio as _a
_pending = [t for t in _a.all_tasks() if t is not _a.current_task() and not t.done()]
if _pending:
    await _a.gather(*_pending, return_exceptions=True)
`;

// Traceur « pas à pas » (style Python Tutor) : ré-exécute le programme sous
// sys.settrace en photographiant, à chaque ligne, les variables et la sortie.
const PY_TRACER = `
class _TraceLimite(BaseException):
    pass

def _resume_valeur(valeur):
    try:
        texte = repr(valeur)
    except Exception:
        texte = "<illisible>"
    if len(texte) > 90:
        texte = texte[:87] + "..."
    return texte

def _executer_trace(code_source, limite=400):
    import sys, io, json
    etapes = []
    sortie = io.StringIO()
    vrai_stdout = sys.stdout

    def variables_du_cadre(frame):
        variables = {}
        for nom, valeur in frame.f_locals.items():
            if nom.startswith("__") or type(valeur).__name__ in ("module", "type"):
                continue
            if callable(valeur):
                variables[nom] = "<fonction " + nom + ">"
                continue
            variables[nom] = _resume_valeur(valeur)
        return variables

    def profondeur_de(frame):
        n = 0
        f = frame.f_back
        while f is not None:
            if f.f_code.co_filename == "<script>":
                n += 1
            f = f.f_back
        return n

    def tracer(frame, evenement, arg):
        if frame.f_code.co_filename != "<script>":
            return None
        if evenement not in ("call", "line", "return", "exception"):
            return tracer
        if len(etapes) >= limite:
            raise _TraceLimite()
        etape = {
            "ligne": frame.f_lineno,
            "evenement": evenement,
            "fonction": frame.f_code.co_name,
            "profondeur": profondeur_de(frame),
            "variables": variables_du_cadre(frame),
            "sortie": sortie.tell(),
        }
        if evenement == "return":
            etape["retour"] = _resume_valeur(arg)
        if evenement == "exception":
            etape["erreur"] = arg[0].__name__ + ": " + str(arg[1])
        etapes.append(etape)
        return tracer

    erreur = None
    tronquee = False
    sys.stdout = sortie
    try:
        objet_code = compile(code_source, "<script>", "exec")
        espace = {"__name__": "__main__"}
        sys.settrace(tracer)
        try:
            exec(objet_code, espace)
        finally:
            sys.settrace(None)
    except _TraceLimite:
        tronquee = True
    except BaseException as e:
        erreur = type(e).__name__ + ": " + str(e)
    finally:
        sys.stdout = vrai_stdout

    return json.dumps({
        "etapes": etapes,
        "sortie": sortie.getvalue(),
        "erreur": erreur,
        "tronquee": tronquee,
    })
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

// Paquets : deux mécanismes complémentaires, comme un `pip install` automatique.
// 1) loadPackagesFromImports : lit les `import` du code et télécharge les paquets
//    que Pyodide fournit compilés pour le navigateur (numpy, pandas, matplotlib…) ;
// 2) si l'exécution échoue avec ModuleNotFoundError : micropip tente d'installer
//    le paquet depuis PyPI (fonctionne pour les paquets en pur Python).
async function chargerPaquets(py, code, ui) {
  try {
    await py.loadPackagesFromImports(code, { messageCallback: (m) => ui.status(m) });
  } catch { /* module inconnu de Pyodide : micropip prendra le relais */ }
}

async function installerDepuisPyPI(py, paquet, ui) {
  ui.print(`📦 « ${paquet} » n'est pas encore disponible — téléchargement depuis PyPI…`, "sys");
  ui.status(`Installation de ${paquet}…`);
  await py.loadPackage("micropip");
  const micropip = py.pyimport("micropip");
  try {
    await micropip.install(paquet);
    ui.print(`📦 « ${paquet} » installé ✅ — on relance ton programme.`, "sys");
  } finally {
    micropip.destroy();
  }
}

// options.keepNamespace : renvoie { output, ns } et NE détruit pas l'espace de
// noms final, pour que le terminal interactif puisse continuer d'y accéder
// (appeler les fonctions de l'exercice, inspecter les variables…).
async function runPython(code, ui, options = {}) {
  const t0 = performance.now();
  ui.clear();
  ui.status("Préparation…");
  const emballe = (output, ns) => options.keepNamespace ? { output, ns } : output;
  let py;
  try {
    py = await ensurePyodide(ui.status);
  } catch (e) {
    ui.print("❌ " + e.message, "err");
    ui.status("");
    return emballe(null, null);
  }
  await chargerPaquets(py, code, ui);
  ui.status("Exécution…");
  py.setStdout({ batched: (s) => ui.print(s) });
  py.setStderr({ batched: (s) => ui.print(s, "err") });

  let output = null;
  // Espace de noms neuf à chaque exécution (comme relancer `python fichier.py`).
  let ns = py.globals.get("dict")();
  ns.set("__name__", "__main__");
  for (let tentative = 0; tentative < 3; tentative++) {
    try {
      await py.runPythonAsync(code, { globals: ns });
      await py.runPythonAsync(PY_DRAIN);
      output = ui.text();
      break;
    } catch (e) {
      const manquant = String(e.message || e).match(/ModuleNotFoundError: No module named '([A-Za-z0-9_.]+)'/);
      if (manquant && tentative < 2) {
        const paquet = manquant[1].split(".")[0];
        try {
          await installerDepuisPyPI(py, paquet, ui);
          ns.destroy();                   // on repart d'un espace de noms neuf
          ns = py.globals.get("dict")();
          ns.set("__name__", "__main__");
          continue;                       // on retente l'exécution
        } catch {
          ui.print(`❌ « ${paquet} » n'a pas pu être installé dans le navigateur `
            + `(paquet avec du code compilé non porté en WebAssembly ?).\n`
            + `   Sur ta machine, ce serait :  pip install ${paquet}`, "err");
          break;
        }
      }
      ui.print(formatPyError(e), "err");
      break;
    }
  }
  const dt = ((performance.now() - t0) / 1000).toFixed(1);
  ui.status(`Terminé en ${dt} s`);
  if (options.keepNamespace) return { output, ns };
  ns.destroy();
  return output;
}

// Exécute UNE saisie du terminal interactif dans l'espace de noms persistant de
// l'IDE (getNs). N'efface pas la console : on ajoute au fil, comme un vrai shell.
async function runTerminalLine(code, ui, getNs) {
  let py;
  try {
    py = await ensurePyodide(ui.status);
  } catch (e) {
    ui.print("❌ " + e.message, "err");
    ui.status("");
    return;
  }
  await chargerPaquets(py, code, ui);
  py.setStdout({ batched: (s) => ui.print(s) });
  py.setStderr({ batched: (s) => ui.print(s, "err") });
  const espace = getNs(py);
  const executer = py.globals.get("_pyguide_terminal");
  try {
    executer(code, espace);
  } catch (e) {
    ui.print(formatPyError(e), "err");
  } finally {
    executer.destroy();
    ui.status("");
  }
}

async function tracerPython(code, ui) {
  let py;
  try {
    py = await ensurePyodide(ui.status);
  } catch (e) {
    ui.print("❌ " + e.message, "err");
    return null;
  }
  await chargerPaquets(py, code, ui);
  ui.status("Enregistrement de la trace…");
  try {
    py.globals.set("_code_a_tracer", code);
    const brut = await py.runPythonAsync(PY_TRACER + "\n_executer_trace(_code_a_tracer)");
    return JSON.parse(brut);
  } catch (e) {
    ui.print(formatPyError(e), "err");
    return null;
  } finally {
    ui.status("");
  }
}

function formatPyError(e) {
  // On ne garde que la partie utile de la traceback (pas les couches Pyodide ni
  // notre passe-plat interne). Le code de l'utilisateur porte l'un de ces noms
  // de fichier ; on coupe au premier cadre correspondant. « <terminal> » est
  // prioritaire : quand il est présent, « <exec> » n'est que le passe-plat du
  // terminal (_pyguide_terminal) et doit rester masqué.
  const msg = String(e.message || e);
  const reperes = ['File "<terminal>"', 'File "<script>"', 'File "<exec>"', 'File "<string>"'];
  for (const repere of reperes) {
    const idx = msg.indexOf(repere);
    if (idx >= 0) return "❌ Erreur Python :\n" + msg.slice(idx);
  }
  return "❌ " + msg;
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
      <button class="btn btn-ghost" data-act="trace"
        title="Exécute ligne par ligne : tu VOIS les variables changer">🔍 Pas à pas</button>
      ${(options.extraButtons || []).map((b, i) =>
        `<button class="btn btn-ghost" data-extra="${i}">${b.label}</button>`).join("")}
      <button class="btn btn-ghost" data-act="reset" title="Revenir au code d'origine">↺</button>
      <span class="spacer"></span>
      <span class="ide-status"></span>
    </div>
    <div class="editor-wrap"><textarea></textarea></div>
    <div class="score-slot"></div>
    <div class="console"><span class="sys placeholder">La sortie de ton programme s'affichera ici. Appuie sur ▶ Exécuter.</span></div>
    <div class="terminal">
      <div class="terminal-head">⌨️ Terminal Python — tape une commande et appuie sur Entrée
        <span class="terminal-hint">(Maj+Entrée = nouvelle ligne)</span></div>
      <div class="terminal-line">
        <span class="terminal-prompt">&gt;&gt;&gt;</span>
        <textarea class="terminal-input" rows="1" spellcheck="false" autocapitalize="off"
          autocomplete="off" autocorrect="off" placeholder="ex : 2 + 2   ou   help(str)"></textarea>
      </div>
    </div>`;

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

  // Espace de noms partagé entre « ▶ Exécuter » et le terminal interactif :
  // après avoir lancé son code, l'apprenant peut appeler ses fonctions et
  // inspecter ses variables directement dans le terminal ci-dessous.
  let terminalNs = null;
  const ensureTerminalNs = (py) => {
    if (!terminalNs) {
      terminalNs = py.globals.get("dict")();
      terminalNs.set("__name__", "__main__");
    }
    return terminalNs;
  };
  const adopterNs = (ns) => {
    if (!ns) return;
    if (terminalNs) terminalNs.destroy();
    terminalNs = ns;
  };

  const runBtn = $('[data-act="run"]', host);
  runBtn.addEventListener("click", async () => {
    runBtn.disabled = true;
    const { output, ns } = await runPython(cm.getValue(), ui, { keepNamespace: true });
    adopterNs(ns);
    runBtn.disabled = false;
    if (output !== null && options.onScore) {
      const m = output.match(/(\d+)\s*\/\s*(\d+)\s+réussis/);
      if (m) options.onScore(Number(m[1]), Number(m[2]), host);
    }
  });

  // ── Terminal interactif (REPL) ──────────────────────────────────────
  const termInput = $(".terminal-input", host);
  const history = [];
  let histIndex = 0;              // position dans l'historique (== longueur = saisie neuve)
  const autoGrow = () => {
    termInput.style.height = "auto";
    termInput.style.height = Math.min(termInput.scrollHeight, 160) + "px";
  };
  const echoTerminal = (src) => {
    const ligne = src.split("\n").map((l, i) => (i ? "... " : ">>> ") + l).join("\n");
    ui.print(ligne, "echo");
  };
  const soumettreTerminal = async (src) => {
    const ph = consoleEl.querySelector(".placeholder");
    if (ph) ph.remove();
    history.push(src);
    histIndex = history.length;
    echoTerminal(src);
    termInput.value = "";
    autoGrow();
    termInput.disabled = true;
    await runTerminalLine(src, ui, ensureTerminalNs);
    termInput.disabled = false;
    termInput.focus();
    consoleEl.scrollTop = consoleEl.scrollHeight;
  };
  termInput.addEventListener("input", autoGrow);
  termInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      const src = termInput.value.replace(/\s+$/, "");
      if (src.trim()) soumettreTerminal(src);
      return;
    }
    // Historique : flèches ↑/↓ quand la saisie tient sur une seule ligne.
    if ((e.key === "ArrowUp" || e.key === "ArrowDown") && !termInput.value.includes("\n")) {
      if (e.key === "ArrowUp" && histIndex > 0) {
        e.preventDefault();
        histIndex--;
        termInput.value = history[histIndex];
        autoGrow();
      } else if (e.key === "ArrowDown" && histIndex < history.length) {
        e.preventDefault();
        histIndex++;
        termInput.value = history[histIndex] ?? "";
        autoGrow();
      }
    }
  });

  const traceBtn = $('[data-act="trace"]', host);
  traceBtn.addEventListener("click", async () => {
    traceBtn.disabled = true;
    const data = await tracerPython(cm.getValue(), ui);
    traceBtn.disabled = false;
    if (data) montrerTrace(data, cm, host);
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

/* ─────────── Visionneuse « pas à pas » (style Python Tutor) ─────────── */

function fermerTrace(cm, host) {
  const panel = $(".trace-panel", host);
  if (panel) panel.remove();
  if (cm._traceLine != null) {
    cm.removeLineClass(cm._traceLine, "background", "cm-trace-line");
    cm._traceLine = null;
  }
}

function labelEtape(e) {
  if (e.evenement === "call") {
    return e.fonction === "<module>" ? "▶ Début du programme"
      : `▶ On ENTRE dans ${e.fonction}()`;
  }
  if (e.evenement === "return") {
    return e.fonction === "<module>" ? "⏹ Fin du programme"
      : `◀ ${e.fonction}() se termine et RENVOIE ${e.retour ?? "None"}`;
  }
  if (e.evenement === "exception") return "⚠️ " + e.erreur;
  return `Ligne ${e.ligne}` + (e.fonction !== "<module>" ? ` — dans ${e.fonction}()` : "");
}

function montrerTrace(data, cm, host) {
  fermerTrace(cm, host);
  const n = data.etapes.length;
  const panel = document.createElement("div");
  panel.className = "trace-panel";

  if (n === 0) {
    panel.innerHTML = `<div class="trace-event">${data.erreur
      ? "⚠️ " + escapeHtml(data.erreur) : "Rien à exécuter (code vide ?)"}
      </div><div style="text-align:right"><button class="btn btn-ghost" data-t="close">Fermer</button></div>`;
    $(".editor-wrap", host).after(panel);
    $('[data-t="close"]', panel).addEventListener("click", () => fermerTrace(cm, host));
    return;
  }

  panel.innerHTML = `
    <div class="trace-controls">
      <button class="tbtn" data-t="first" title="Première étape">⏮</button>
      <button class="tbtn" data-t="prev" title="Étape précédente">◀</button>
      <input type="range" min="0" max="${n - 1}" value="0" step="1" aria-label="Étape">
      <button class="tbtn" data-t="next" title="Étape suivante">▶</button>
      <button class="tbtn" data-t="last" title="Dernière étape">⏭</button>
      <span class="trace-pos"></span>
      <button class="tbtn" data-t="close" title="Fermer">✕</button>
    </div>
    <div class="trace-event"></div>
    <div class="trace-vars"></div>
    <pre class="trace-out"></pre>
    ${data.tronquee ? '<div class="trace-note">✂️ Programme long : seules les 400 premières étapes sont montrées.</div>' : ""}
    ${data.erreur ? `<div class="trace-note">⚠️ Le programme s'est terminé par une erreur : ${escapeHtml(data.erreur)}</div>` : ""}`;
  $(".editor-wrap", host).after(panel);

  const slider = $('input[type="range"]', panel);
  let index = 0;

  function setStep(k) {
    index = Math.max(0, Math.min(n - 1, k));
    slider.value = index;
    const e = data.etapes[index];
    $(".trace-pos", panel).textContent = `${index + 1}/${n}`;
    $(".trace-event", panel).textContent = labelEtape(e);

    // surligne la ligne en cours dans l'éditeur (l'événement « début du
    // programme » porte la ligne 0, et le code a pu être raccourci depuis)
    if (cm._traceLine != null) cm.removeLineClass(cm._traceLine, "background", "cm-trace-line");
    cm._traceLine = Math.min(Math.max(e.ligne, 1), cm.lineCount()) - 1;
    cm.addLineClass(cm._traceLine, "background", "cm-trace-line");
    cm.scrollIntoView({ line: cm._traceLine, ch: 0 }, 80);

    // variables visibles à cette étape
    const noms = Object.keys(e.variables);
    const cadre = e.fonction === "<module>" ? "programme principal" : e.fonction + "()";
    $(".trace-vars", panel).innerHTML = noms.length
      ? `<div class="trace-cadre">Variables — ${escapeHtml(cadre)}</div><table>${noms.map((nom) =>
          `<tr><td>${escapeHtml(nom)}</td><td>${escapeHtml(e.variables[nom])}</td></tr>`).join("")}</table>`
      : `<div class="trace-cadre">Aucune variable pour l'instant (${escapeHtml(cadre)})</div>`;

    // sortie déjà affichée à cette étape
    const texte = data.sortie.slice(0, e.sortie);
    const out = $(".trace-out", panel);
    out.textContent = texte;
    out.style.display = texte ? "" : "none";
  }

  $('[data-t="first"]', panel).addEventListener("click", () => setStep(0));
  $('[data-t="prev"]', panel).addEventListener("click", () => setStep(index - 1));
  $('[data-t="next"]', panel).addEventListener("click", () => setStep(index + 1));
  $('[data-t="last"]', panel).addEventListener("click", () => setStep(n - 1));
  $('[data-t="close"]', panel).addEventListener("click", () => fermerTrace(cm, host));
  slider.addEventListener("input", () => setStep(Number(slider.value)));

  setStep(0);
  panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function showScore(ok, total, host) {
  const slot = $(".score-slot", host);
  const win = ok === total;
  slot.innerHTML = `<div class="score-banner ${win ? "win" : "partial"}">
    ${win ? "🎉 Bravo, " : "💪 Continue : "} ${ok}/${total} exercices réussis${win ? " !" : "."}
  </div>`;
}

/* ─────────────────────────── Quiz (QCM auto-corrigé) ─────────────────────────── */

function viewQuiz(host, mod) {
  const quiz = mod.quiz;
  const inline = (t) => marked.parseInline(t, { mangle: false });
  host.innerHTML = `
    <div class="ide-note">🧠 <div>Vérifie ta compréhension : une réponse par question, puis
      « Valider ». Tu verras la correction et une explication. (Rien à installer, pas de code.)</div></div>
    <form class="quiz">
      ${quiz.map((q, i) => `
        <fieldset class="quiz-q" data-i="${i}">
          <legend><span class="quiz-num">${i + 1}</span> ${inline(q.q)}</legend>
          <div class="quiz-opts">
            ${q.options.map((opt, j) => `
              <label class="quiz-opt">
                <input type="radio" name="q${i}" value="${j}">
                <span>${inline(opt)}</span>
              </label>`).join("")}
          </div>
          <div class="quiz-expl" hidden>💡 ${inline(q.explanation || "")}</div>
        </fieldset>`).join("")}
      <div class="quiz-actions">
        <button type="button" class="btn btn-primary" data-act="valider-quiz">Valider le quiz</button>
        <button type="button" class="btn btn-ghost" data-act="refaire-quiz" hidden>↺ Refaire</button>
      </div>
      <div class="score-slot"></div>
    </form>`;

  const form = $(".quiz", host);
  const btnValider = $('[data-act="valider-quiz"]', host);
  const btnRefaire = $('[data-act="refaire-quiz"]', host);

  btnValider.addEventListener("click", () => {
    let ok = 0;
    let repondu = 0;
    quiz.forEach((q, i) => {
      const fs = $(`.quiz-q[data-i="${i}"]`, host);
      const choisi = form.querySelector(`input[name="q${i}"]:checked`);
      if (choisi) repondu++;
      fs.querySelectorAll(".quiz-opt").forEach((lab, j) => {
        const input = lab.querySelector("input");
        input.disabled = true;
        lab.classList.toggle("is-correct", j === q.correct);
        lab.classList.toggle("is-wrong", input.checked && j !== q.correct);
      });
      const bon = choisi && Number(choisi.value) === q.correct;
      if (bon) ok++;
      fs.classList.add(bon ? "correct" : "wrong");
      $(".quiz-expl", fs).hidden = false;
    });
    const slot = $(".score-slot", host);
    const parfait = ok === quiz.length;
    slot.innerHTML = `<div class="score-banner ${parfait ? "win" : "partial"}">
      ${parfait ? "🎉 Sans faute — " : "💪 "} ${ok}/${quiz.length} bonnes réponses${
        repondu < quiz.length ? ` (${quiz.length - repondu} sans réponse)` : ""}.
    </div>`;
    progress.update(mod.id, { quiz_ok: ok, quiz_total: quiz.length });
    btnValider.hidden = true;
    btnRefaire.hidden = false;
    slot.scrollIntoView({ behavior: "smooth", block: "nearest" });
  });

  btnRefaire.addEventListener("click", () => viewQuiz(host, mod));
}

/* ─────────────────────────── Vues ─────────────────────────── */

function viewHome() {
  const pct = globalPercent();
  const lastId = store.read("lastModule", null);
  const last = CONTENT.modules.find((m) => m.id === lastId);
  const cont = last
    ? `<a class="btn btn-light" href="#/module/${last.id}">▶ Continuer : ${last.num ? last.num + " · " : ""}${escapeHtml(last.title)}</a>`
    : `<a class="btn btn-light" href="#/module/00_demarrer">▶ Commencer le parcours</a>`;

  const cards = CONTENT.modules.map((m) => {
    const p = progress.of(m.id);
    const sub = p.total > 0 ? `Exercices : ${p.ok}/${p.total} réussis`
      : m.exercices ? "Cours + exercices" : "Lecture + démos";
    return `<a class="card" href="#/module/${m.id}">
      <span class="emoji">${m.emoji}</span>
      <span class="card-body">
        <div class="card-title">${m.num ? m.num + " · " : ""}${escapeHtml(m.title)}</div>
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
      <p>Cours en français, exercices à faire toi-même et un vrai Python intégré —
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
      <a class="card" href="#/pentest"><span class="emoji">🛡️</span>
        <span class="card-body"><div class="card-title">Pentest &amp; sécurité</div>
        <div class="card-sub">Python pour l'audit : réseau, web, recon, crypto, démos offensives (lab)</div></span></a>
    </div>

    <div class="section-title">🧭 Guides de survie</div>
    <div class="cards">${guides}</div>`;
}

function moduleTabs(mod, active) {
  const tabs = [["cours", "📖 Cours"]];
  if (mod.exercices) tabs.push(["exercices", "🧪 Exercices"]);
  if (mod.quiz && mod.quiz.length) tabs.push(["quiz", "🧠 Quiz"]);
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
      <div class="crumbs"><a href="#/">Accueil</a> / ${mod.num ? "Module " + mod.num : "Fondation"}</div>
      <h1>${mod.emoji} ${escapeHtml(mod.title)}</h1>
    </div>
    ${moduleTabs(mod, tab)}
    <div id="tab-content"></div>
    <div class="pager">
      ${prev ? `<a class="btn btn-ghost" href="#/module/${prev.id}">← ${prev.num || "🧭"}</a>` : "<span></span>"}
      ${next ? `<a class="btn btn-primary" href="#/module/${next.id}">${next.num ? "Module " + next.num : "🧭 Penser comme un dev"} →</a>`
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
    const note = mod.note || "Lis la consigne de chaque exercice, écris ton code dans l'espace "
      + "« ✏️ ton code ici », puis ▶ Exécuter et compare ce qui s'affiche au « 👀 Résultat "
      + "attendu » indiqué juste au-dessus. Ton code est sauvegardé sur cet appareil.";
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
  } else if (tab === "quiz") {
    viewQuiz(host, mod);
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

function viewPentest(groupId) {
  const pt = CONTENT.pentest;
  const groupe = groupId ? pt.groupes.find((g) => g.id === groupId) : null;

  const tabs = `<div class="tabs">
    <button class="tab ${!groupe ? "active" : ""}" data-go="#/pentest">🛡️ Aperçu</button>
    ${pt.groupes.map((g) =>
      `<button class="tab ${groupe && groupe.id === g.id ? "active" : ""}"
        data-go="#/pentest/${g.id}">${escapeHtml(g.titre)}</button>`).join("")}</div>`;

  view.innerHTML = `
    <div class="module-head">
      <div class="crumbs"><a href="#/">Accueil</a> / Pentest &amp; sécurité</div>
      <h1>🛡️ Pentest &amp; sécurité</h1>
    </div>
    ${tabs}
    <div class="md" id="pt-md"></div>
    <div id="pt-files"></div>`;

  document.querySelectorAll(".tab").forEach((b) =>
    b.addEventListener("click", () => { location.hash = b.dataset.go; }));

  // Aperçu : le README global (contient les règles d'éthique et la feuille de route).
  if (!groupe) {
    renderMarkdown(pt.readme, $("#pt-md"));
    return;
  }

  if (groupe.readme) renderMarkdown(groupe.readme, $("#pt-md"));

  const host = $("#pt-files");
  host.innerHTML = `
    <div class="section-title">💻 Scripts du module</div>
    <div class="file-pills">${groupe.files.map((f, i) =>
      `<button class="file-pill" data-i="${i}">${escapeHtml(f.name)}</button>`).join("")}</div>
    <div id="pt-ide"></div>`;

  const loadFile = (i) => {
    document.querySelectorAll(".file-pill").forEach((p, j) => p.classList.toggle("active", i === j));
    const f = groupe.files[i];
    createIDE($("#pt-ide"), {
      code: f.code,
      storageKey: "pentest:" + groupe.id + ":" + f.name,
      note: f.note || "✅ Ce script tourne dans le navigateur : clique ▶ Exécuter, "
        + "ou teste tes idées dans le terminal ci-dessous.",
    });
  };
  document.querySelectorAll(".file-pill").forEach((p) =>
    p.addEventListener("click", () => loadFile(Number(p.dataset.i))));
  if (groupe.files.length) loadFile(0);
}

const IDE_DEFAULT = `# ⌨️ Bac à sable — écris du Python, appuie sur ▶ Exécuter.
# Tout tourne DANS ton navigateur : tu ne peux rien casser. Amuse-toi !
#
# 🔍 « Pas à pas » : exécute ligne par ligne en voyant les variables changer.
# 📦 Besoin d'une bibliothèque ? Importe-la simplement (import numpy,
#    import pandas…) : elle sera téléchargée automatiquement.

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
  else if (root === "pentest") { viewPentest(a); highlightNav("pentest"); }
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
