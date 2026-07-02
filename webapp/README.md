# 📱 La plateforme e-learning — Python Guide dans ton navigateur

Ce dossier contient une **application web** (PWA) qui transforme tout le dépôt en
**plateforme d'apprentissage interactive** : les cours, les exercices auto-corrigés
et un **vrai Python** qui s'exécute **dans le navigateur** — ordinateur, tablette
ou **téléphone Android**, sans rien installer.

> 🌐 En ligne : **https://tn-redteam.github.io/Python_guide/** *(une fois GitHub
> Pages activé, voir plus bas)*

---

## ✨ Ce qu'elle sait faire

| Fonction | Détail |
|---|---|
| 📖 **Tous les cours** | Les 16 modules + les 7 guides (symboles, glossaire…) + les mini-projets, rendus joliment (hors pentest, volontairement). |
| ⌨️ **IDE intégré** | Éditeur avec coloration syntaxique (CodeMirror) + **Python 3.12 réel** compilé en WebAssembly ([Pyodide](https://pyodide.org)) : ton code s'exécute localement, dans l'onglet. |
| 🧪 **Exercices auto-corrigés** | Les `exercices.py` de chaque module, préchargés dans l'IDE : tu complètes, tu appuies sur ▶, tu vois tes ✅/❌. Le score est détecté automatiquement. |
| 📊 **Progression** | Sauvegardée sur l'appareil (localStorage) : modules lus, scores d'exercices, reprise là où tu t'étais arrêté. Rien n'est envoyé à un serveur. |
| 💾 **Ton code est conservé** | Chaque éditeur mémorise tes modifications sur l'appareil ; bouton ↺ pour revenir au code d'origine. |
| 📱 **Installable (PWA)** | Sur Android : Chrome → menu ⋮ → « Ajouter à l'écran d'accueil ». L'app s'ouvre alors en plein écran, comme une application native, et les cours restent disponibles hors ligne. |
| 🌙 **Thème sombre / clair** | Bouton en haut à droite. |
| ▶ **« Essayer »** | Chaque bloc de code Python d'un cours a un bouton qui l'envoie dans le bac à sable. |

**Limites honnêtes** (c'est un navigateur, pas ta machine) : pas d'accès réseau
(`requests`), pas de vrais dossiers, pas de `pip install`, pas de débogueur
interactif (`pdb`). Les modules concernés (11, 12, 13, 14…) l'affichent clairement
et restent à pratiquer sur un vrai Python — c'est d'ailleurs le but du parcours.

---

## 🚀 Lancer en local

```bash
# depuis la racine du dépôt :
python3 webapp/build_content.py      # (re)génère content.json depuis les cours
cd webapp
python3 -m http.server 8000          # puis ouvre http://localhost:8000
```

> ⚠️ Ouvrir `index.html` en double-cliquant (`file://`) ne marche pas : le
> navigateur bloque le chargement de `content.json`. Il faut un petit serveur,
> d'où le `http.server` ci-dessus.

Première exécution de code : Pyodide (~10 Mo) est téléchargé depuis le CDN
jsdelivr, puis mis en cache. Les exécutions suivantes sont immédiates.

---

## 🌐 Mettre en ligne (GitHub Pages)

1. Sur GitHub : **Settings → Pages → Source : « GitHub Actions »** (à faire une fois).
2. Le workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml)
   régénère `content.json` et déploie `webapp/` à chaque push sur `main`.
3. L'app est servie sur `https://<organisation>.github.io/Python_guide/`.

---

## 🧩 Comment c'est construit (et pourquoi c'est simple)

```
webapp/
├── index.html            # la page unique (SPA à routage par hash)
├── css/style.css         # design mobile-first, thèmes sombre/clair
├── js/app.js             # routeur, rendu markdown, IDE, Pyodide, progression
├── content.json          # ← GÉNÉRÉ par build_content.py (les cours embarqués)
├── build_content.py      # extrait README/exercices/solutions des modules
├── make_icons.py         # génère les icônes PNG (pur stdlib, zéro dépendance)
├── manifest.webmanifest  # méta-données PWA (installation Android)
├── sw.js                 # service worker : cache hors ligne
├── vendor/               # CodeMirror + marked, embarqués (pas de CDN requis)
└── icons/                # icônes générées
```

Choix assumés :

- **Aucun framework, aucun build** (pas de npm, pas de bundler) : du HTML/CSS/JS
  lisible — cohérent avec la pédagogie du dépôt, et déployable n'importe où.
- **Une seule source de vérité** : la plateforme est *générée* depuis les
  `README.md` / `exercices.py` du dépôt. Corriger un cours = corriger le dépôt,
  puis relancer `build_content.py` (le déploiement le fait tout seul).
- **Tout est local pour l'élève** : progression et code dans le navigateur,
  aucune donnée collectée, aucun compte.

## 🔧 Modifier / contribuer

- Tu as changé un cours ou un exercice ? → `python3 webapp/build_content.py`.
- Tu as changé `index.html` / `app.js` / `style.css` ? → incrémente `VERSION`
  dans `sw.js` pour que les visiteurs reçoivent la mise à jour hors ligne.
- Icônes : `python3 webapp/make_icons.py`.
