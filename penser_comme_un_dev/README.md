# 🧭 Penser comme un dev : la logique avant la syntaxe

:::objectif Ce que tu vas gagner ici
Avant d'apprendre *quoi taper*, apprends **comment réfléchir**. Ce module te
donne une **méthode** pour attaquer n'importe quel problème : le comprendre, le
**découper**, écrire les **étapes** (pseudo-code), puis seulement le traduire en
Python. C'est la compétence qui fait la différence entre « connaître la syntaxe »
et « savoir programmer ».
:::

> 🧠 **L'idée-clé du module** : un programme n'est pas un texte à mémoriser,
> c'est un **raisonnement** que tu poses par écrit. La syntaxe, tu l'oublieras et
> la re-chercheras toute ta vie. Le raisonnement, lui, se muscle — et il se
> transfère à **tous** les langages.

---

## 1. Coder, c'est d'abord penser

Un ordinateur est **rapide mais bête** : il fait *exactement* ce que tu écris,
dans l'ordre, sans deviner ton intention. Programmer, ce n'est donc pas parler à
une machine intelligente — c'est **décrire une marche à suivre** si précise qu'un
exécutant sans cerveau pourrait la dérouler.

:::idee La bonne analogie
C'est une **recette de cuisine** pour quelqu'un qui n'a jamais cuisiné. « Fais un
gâteau » ne suffit pas. Il faut : *casser 3 œufs, ajouter 200 g de sucre,
mélanger 2 minutes…*. Chaque étape est **petite, ordonnée et sans ambiguïté**.
Le code, c'est ça.
:::

La conséquence est libératrice : **si tu sais décrire les étapes en français, tu
sais programmer**. Le reste (la syntaxe Python) n'est qu'une question de
traduction, et un moteur de recherche t'aide pour la traduction.

---

## 2. La méthode : les 4 temps

Face à **n'importe quel** problème, ne saute jamais directement au clavier.
Suis toujours ces 4 temps, dans l'ordre :

| # | Temps | La question qu'on se pose |
|---|-------|---------------------------|
| 1 | **Comprendre** | Qu'est-ce qu'on me donne ? Qu'est-ce que je dois produire ? |
| 2 | **Décomposer** | En quelles petites étapes je peux couper ça ? |
| 3 | **Pseudo-code** | J'écris les étapes en français, dans l'ordre. |
| 4 | **Traduire & tester** | Je passe chaque étape en Python, puis je vérifie. |

:::piege L'erreur du débutant
Coder **avant** d'avoir compris et décomposé. On tape, ça plante, on retape au
hasard… et on tourne en rond. **90 % du travail se fait sans toucher au
clavier.** Le clavier, c'est la dernière étape, pas la première.
:::

Déroulons les 4 temps sur un exemple fil rouge :

> 🎯 **Problème fil rouge** : « À partir d'une liste de notes sur 20, calcule la
> **moyenne** de la classe. »

---

## 3. Temps 1 — Comprendre

Comprendre, c'est répondre à 3 questions, **par écrit** :

1. **Entrée** : qu'est-ce que je reçois ? → *une liste de nombres* (`[12, 8, 15]`).
2. **Sortie** : qu'est-ce que je dois renvoyer ? → *un seul nombre* (la moyenne).
3. **Exemple** : un cas concret que je sais résoudre à la main.

:::astuce Le jeu d'essai : ton filet de sécurité
Invente **toujours** un petit exemple dont tu connais déjà la réponse :

`[12, 8, 16]` → total `36`, divisé par `3` notes → **moyenne 12**.

Cet exemple va te servir à (a) vérifier que tu as compris, et (b) tester ton code
à la fin. Si tu ne sais pas résoudre l'exemple **à la main**, tu ne pourras pas
l'écrire en code.
:::

---

## 4. Temps 2 — Décomposer

Un gros problème fait peur. **Un petit problème, non.** L'art, c'est de couper le
gros en petits, jusqu'à ce que chaque morceau soit évident.

« Calculer une moyenne » se découpe en :

:::etape Découpage du problème
1. Faire la **somme** de toutes les notes.
2. **Compter** combien il y a de notes.
3. **Diviser** la somme par le nombre de notes.
:::

Chaque morceau est maintenant une action simple. On sait faire chacune
séparément — c'est ça, décomposer.

> 🧠 **Le réflexe à prendre** : « une seule chose à la fois ». Si une étape est
> encore trop grosse ou trop floue, **re-découpe-la**. On s'arrête quand chaque
> étape tient en une phrase claire.

---

## 5. Temps 3 — Le pseudo-code

Le **pseudo-code**, c'est écrire les étapes en **français structuré** — la
logique, sans se soucier de la syntaxe Python. On raisonne ; on ne code pas
encore.

```pseudo
FONCTION moyenne(notes) :
    total  ← 0
    POUR chaque note DANS notes :
        total ← total + note        # on accumule
    nombre ← combien d'éléments dans notes
    RENVOYER total / nombre
```

:::idee Pourquoi passer par là ?
Parce que réfléchir **et** se battre avec la syntaxe **en même temps**, c'est
deux fois trop d'effort. Le pseudo-code isole la partie difficile (le
raisonnement). Une fois qu'il est juste, la traduction en Python est presque
mécanique.
:::

---

## 6. Temps 4 — Traduire & tester

Maintenant seulement, on traduit **ligne à ligne** le pseudo-code en Python :

```python
def moyenne(notes):
    total = 0
    for note in notes:
        total = total + note      # on accumule (voir "patterns" plus bas)
    nombre = len(notes)
    return total / nombre

# On TESTE avec notre jeu d'essai : on connaît déjà la réponse (12).
print(moyenne([12, 8, 16]))       # 12.0  ✅
```

Tu remarques la correspondance **1 ligne de pseudo-code = 1 ligne de Python**.
C'est le signe qu'on a bien travaillé en amont.

:::astuce Teste petit, teste tôt
N'écris pas 40 lignes avant de lancer. Écris 3 lignes, lance, vérifie, continue.
Un bug trouvé tout de suite se corrige en 10 secondes ; le même bug noyé dans
40 lignes te coûte 20 minutes.
:::

---

## 7. Les 5 patterns qui reviennent *tout le temps*

90 % des petits programmes réutilisent les **mêmes 5 schémas**. Reconnais-les, et
la moitié du travail de décomposition est déjà faite.

:::etape 1. L'accumulateur — « faire un total »
On part d'un total à `0`, et on **ajoute** au fur et à mesure.
```python
total = 0
for x in nombres:
    total = total + x
```
Sert à : somme, produit, concaténer un texte, tout empiler.
:::

:::etape 2. Le compteur — « combien y en a-t-il ? »
Comme l'accumulateur, mais on ajoute `1` **quand une condition est vraie**.
```python
compte = 0
for x in nombres:
    if x > 10:
        compte = compte + 1
```
:::

:::etape 3. La recherche + drapeau — « est-ce qu'il existe… ? »
Un **booléen** qui démarre à `False` et passe à `True` si on trouve.
```python
trouve = False
for x in nombres:
    if x == cible:
        trouve = True
```
:::

:::etape 4. Le filtre — « garder seulement ceux qui… »
On construit une **nouvelle liste** en ne gardant que les bons.
```python
gardes = []
for x in nombres:
    if x % 2 == 0:
        gardes.append(x)
```
:::

:::etape 5. Le champion (max / min) — « le plus grand / petit »
On retient le **meilleur vu jusqu'ici**, et on le met à jour.
```python
meilleur = nombres[0]
for x in nombres:
    if x > meilleur:
        meilleur = x
```
:::

> 🧠 **Devant un problème, demande-toi** : « est-ce que je dois *totaliser*,
> *compter*, *chercher*, *filtrer* ou *comparer* ? » La réponse t'indique le
> pattern — donc le squelette du code.

---

## 8. Tracer à la main : le super-pouvoir

Quand un code te résiste, **déroule-le à la main** comme le ferait l'ordinateur :
une ligne à la fois, en notant la valeur de **chaque variable** dans un tableau.

Traçons `total` pour `moyenne([12, 8, 16])` :

| Étape | `note` | `total` avant | `total` après |
|-------|--------|---------------|---------------|
| début | —      | —             | `0` |
| tour 1 | `12`  | `0`           | `12` |
| tour 2 | `8`   | `12`          | `20` |
| tour 3 | `16`  | `20`          | `36` |
| fin   | —      | `36`          | → `36 / 3 = 12.0` |

:::astuce L'outil « Pas à pas » fait ça pour toi
Dans l'onglet **Exercices** et le **Bac à sable**, le bouton **🔍 Pas à pas**
déroule ton programme ligne par ligne en te montrant les variables changer —
c'est exactement cette table de suivi, en automatique. Utilise-le sans modération.
:::

---

## 9. Penser aux cas limites

Ton code marche sur l'exemple « normal ». Mais que se passe-t-il aux
**extrêmes** ? C'est là que se cachent les bugs.

:::piege La checklist des cas limites
Avant de dire « c'est fini », teste :

- le **vide** : une liste `[]`, un texte `""` → `moyenne([])` **divise par zéro** !
- le **zéro** et les **négatifs** : `0`, `-5`.
- **un seul** élément : `[10]`.
- le **très grand** ou le **doublon** : `[7, 7, 7]`.

Notre `moyenne` plante sur `[]`. Un vrai dev **prévoit** ce cas :
```python
def moyenne(notes):
    if not notes:              # liste vide ?
        return 0               # on décide d'une réponse sensée
    return sum(notes) / len(notes)
```
:::

---

## 10. Quand ça casse : lire l'erreur

Une erreur (`Traceback`) n'est pas une punition, c'est un **indice précis**.
Python te dit **où** (le numéro de ligne) et **quoi** (le type d'erreur).

> 🔎 **La règle** : lis toujours la **dernière ligne** en premier (le type et le
> message), puis remonte au **numéro de ligne** indiqué. `ZeroDivisionError`,
> `IndexError`, `TypeError`, `NameError`… chacun raconte une histoire courte.
> Le module [🐞 Débugger](../07_debugger) en fait tout un art.

---

## ✅ Récap : la méthode en une image

:::reussi À retenir
1. **Comprends** : entrée → sortie, avec un jeu d'essai.
2. **Décompose** : coupe en petites étapes évidentes.
3. **Pseudo-code** : écris la logique en français.
4. **Traduis & teste** : ligne à ligne, teste petit et tôt.
5. **Vérifie les cas limites**, et lis les erreurs comme des indices.
:::

:::defi À toi de jouer
Passe à l'onglet **🧪 Exercices** : tu vas coder les **5 patterns** de tes propres
mains (total, compteur, recherche, filtre, champion). Pour chacun, fais d'abord le
pseudo-code dans ta tête, **puis** écris le Python. C'est en forgeant…
:::

> ➡️ **La suite** : le module [🏗️ Les bases](../01_les_bases) te donne la syntaxe
> Python (variables, conditions, boucles) pour équiper cette façon de penser.
