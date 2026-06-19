# 🔬 Python vs les autres langages

Tu apprends Python — mais savais-tu que les **concepts** que tu maîtrises (variable, condition,
boucle, fonction) sont **universels** ? Ils existent dans *tous* les langages : seule la
**façon de les écrire** (la syntaxe) change.

> 🧠 **Pourquoi cette page ?** Pour deux raisons :
> 1. te montrer que **ce que tu apprends en Python se réinvestit partout** — ton 2ᵉ langage sera
>    bien plus rapide à apprendre que le 1ᵉʳ ;
> 2. t'aider à **lire** un bout de code croisé sur le web même s'il n'est pas en Python.

On compare ici Python à : Bash, PowerShell, Go, C++, C et l'Assembleur — rangés du plus proche
de l'humain au plus proche de la machine.

---

## 0. Lancer le programme

| Langage | Commande | Compilé ? |
|---------|----------|-----------|
| 🐍 **Python** | `python3 fichier.py` | non (interprété) |
| 🐚 Bash | `bash fichier.sh` | non |
| 🟦 PowerShell | `pwsh fichier.ps1` | non |
| 🐹 Go | `go run fichier.go` | oui (compile + exécute) |
| ➕ C++ | `g++ fichier.cpp -o prog && ./prog` | oui |
| 🇨 C | `gcc fichier.c -o prog && ./prog` | oui |
| ⚙️ Asm | `as f.s -o f.o && ld f.o -o prog && ./prog` | oui (assemblage) |

> 💡 **Python est interprété** : tu lances le fichier directement, sans étape de compilation.
> C'est l'une des raisons qui en font un langage idéal pour débuter.

---

## 1. Afficher « Bonjour »

**Python**
```python
print("Bonjour")
```
**Bash**
```bash
echo "Bonjour"
```
**Go**
```go
package main
import "fmt"
func main() { fmt.Println("Bonjour") }
```
**C**
```c
#include <stdio.h>
int main(void) { printf("Bonjour\n"); return 0; }
```
**Assembleur** (x86-64, simplifié)
```asm
.intel_syntax noprefix
.data
msg: .ascii "Bonjour\n"
.text
.global _start
_start:
    mov rax, 1      # syscall write
    mov rdi, 1      # sortie écran
    lea rsi, [msg]  # adresse du texte
    mov rdx, 8      # nombre d'octets
    syscall
    mov rax, 60     # syscall exit
    mov rdi, 0
    syscall
```

> Mesure l'écart : ce qui tient en **1 ligne** en Python demande de piloter **registre par
> registre** en assembleur. Plus un langage est « bas niveau », plus tu dois tout détailler.

---

## 2. Une variable

| Langage | Code | Remarque |
|---------|------|----------|
| 🐍 **Python** | `age = 30` | type **deviné** automatiquement |
| Bash | `age=30` | ⚠️ **aucun espace** autour du `=` ; lu via `"$age"` |
| PowerShell | `$age = 30` | le nom commence par `$` |
| Go | `age := 30` | type deviné, mais **statique** (fixé une fois) |
| C / C++ | `int age = 30;` | type **déclaré** + `;` obligatoire |
| Asm | `mov rax, 30` | une valeur **dans un registre** |

> En Python, tu n'annonces jamais le type : c'est le **typage dynamique**. En C/Go, le type est
> fixé à la déclaration (**typage statique**) — plus verbeux, mais des erreurs détectées plus tôt.

---

## 3. Une condition

**Python**
```python
if note >= 10:
    print("Reçu")
else:
    print("Recalé")
```
**Go**
```go
if note >= 10 {
    fmt.Println("Reçu")
} else {
    fmt.Println("Recalé")
}
```
**C / C++**
```c
if (note >= 10) {
    printf("Recu\n");
} else {
    printf("Recale\n");
}
```
**Assembleur** : pas de `if` — on **compare** puis on **saute** :
```asm
    cmp rax, 10     # compare note (rax) à 10
    jl  recale      # "jump if less" : si < 10, saute à recale
    # ... cas "Reçu" ...
recale:
    # ... cas "Recalé" ...
```

> Idée commune partout : « selon une comparaison, faire ceci ou cela ». Remarque que Python se
> passe d'accolades `{ }` : c'est l'**indentation** qui délimite le bloc. En assembleur, le `if`
> n'existe pas : il se reconstruit avec **comparer (`cmp`) + sauter (`jl`, `jne`…)**.

---

## 4. Une boucle (répéter 3 fois)

| Langage | Code |
|---------|------|
| 🐍 **Python** | `for i in range(3):` |
| Bash | `for i in {1..3}; do ... done` |
| PowerShell | `for ($i = 0; $i -lt 3; $i++) { }` |
| Go | `for i := 0; i < 3; i++ {` |
| C / C++ | `for (int i = 0; i < 3; i++) {` |

> Le `for` des autres langages dit explicitement « initialise un compteur, teste, avance ».
> Le `for ... in range(...)` de Python cache cette mécanique : plus simple à lire, même idée.

---

## 5. Une fonction qui additionne

**Python**
```python
def add(a, b):
    return a + b
```
**Go**
```go
func add(a int, b int) int {
    return a + b
}
```
**C / C++**
```c
int add(int a, int b) {
    return a + b;
}
```
**Assembleur**
```asm
add:
    mov rax, rdi    # 1er argument
    add rax, rsi    # + 2e argument -> résultat dans rax
    ret             # revient à l'appelant
```

> Partout, une fonction = « un bloc nommé qui prend des entrées et renvoie une sortie ». En
> Python tu ne précises pas les types des paramètres ; en C/Go si. En assembleur, les arguments
> arrivent dans des **registres** (`rdi`, `rsi`) et le résultat repart dans `rax`.

---

## 6. Les commentaires

| Langage | Une ligne | Plusieurs lignes |
|---------|-----------|------------------|
| 🐍 **Python** | `# ...` | `""" ... """` (docstring) |
| Bash | `# ...` | (ligne par ligne) |
| PowerShell | `# ...` | `<# ... #>` |
| Go / C++ / C | `// ...` | `/* ... */` |
| Asm | `# ...` | (ligne par ligne) |

---

## 7. Ce qui change vraiment d'un langage à l'autre

| Critère | 🐍 Python | Bash | Go | C++ | C | Asm |
|---------|-----------|------|----|-----|---|-----|
| Compilation | non | non | oui | oui | oui | oui |
| Typage | dynamique | faible (texte) | statique | statique | statique | registres |
| Gestion mémoire | **automatique** | automatique | automatique | manuelle/outillée | **manuelle** | **totale (toi)** |
| Niveau | très haut | haut | haut | moyen | bas | le plus bas |
| Facilité débutant | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| Point fort | données, web, IA, scripts | automatiser le terminal | serveurs, outils | logiciels exigeants | système | matériel |

---

## 🎯 Quel langage pour quelle tâche ?

Il n'y a pas de « meilleur » langage : il y a le **bon outil pour le bon travail**.

| Ta tâche | Langage conseillé |
|----------|-------------------|
| Débuter la programmation | 🐍 **Python** |
| Automatiser fichiers / données, scraping, web, IA | 🐍 **Python** |
| Automatiser **Linux/macOS**, traiter des logs | 🐚 Bash |
| Automatiser / administrer **Windows** | 🟦 PowerShell |
| Serveurs réseau, outils CLI, conteneurs/cloud | 🐹 Go |
| Logiciels très performants, jeux, moteurs | ➕ C++ |
| Systèmes embarqués, OS, pilotes | 🇨 C |
| Comprendre la machine, reverse engineering | ⚙️ Assembleur |
| Performance **et** sûreté mémoire | 🦀 Rust |

> 🧭 **La règle simple** : tu débutes → **Python**. Tu automatises Unix → Bash. Windows →
> PowerShell. Tu veux de la performance ou un binaire à distribuer → Go, puis C++/C. Tu veux
> comprendre la machine → C, puis l'Assembleur.

---

## 🧭 À retenir

Les **concepts sont universels**. Chaque fois que tu apprends quelque chose en Python (une
boucle, une fonction, une condition), tu l'as **déjà à moitié appris** dans tous les autres
langages — il ne te restera que la syntaxe à adapter.

C'est pour ça qu'**apprendre un 2ᵉ langage est bien plus rapide que le premier**. Continue à
fond sur Python : tu te construis des fondations qui serviront partout.
