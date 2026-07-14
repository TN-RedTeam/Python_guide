# Tests de la plateforme (webapp/)

Test de **fumée** Playwright : il vérifie que l'app se charge, navigue et rend
correctement (accueil, module + encadrés, onglet exercices, pentest, bac à
sable) **sans erreur JS**. Il n'exécute **pas** Pyodide → rapide et fiable, sans
dépendre d'un CDN.

## Lancer

```bash
cd webapp/tests
npm install
npx playwright install chromium
node smoke.mjs
```

Le test sert lui-même `webapp/` (via `python3 -m http.server`) puis l'arrête.

En CI, c'est le job **`webapp`** de [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).

> 💡 En local avec une install Node/Playwright globale, tu peux éviter le
> `npm install` :
> ```bash
> PW_REQUIRE=/chemin/vers/node_modules/playwright \
> PW_EXECUTABLE=/chemin/vers/chromium \
> node smoke.mjs
> ```
