# TP1 - S2 d'Algorithmique : Algorithmes de Graphes & Structures de Données

## 📦 Installation

1. Clone ce dépôt :
```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet
```

# Configuration du json



# Exercice 1 : Recherche et Parcours de Graphes
## Le [BFS](./algos/bfs.py)
1. Execution
```bash
python main.py bfs
```
2. Temps d'éxécution

Le BFS s'éxecute en 0.99ms avec le graphe donné

3. Compléxité

Le BFS a une complexité temporelle de O(V + E) où V est le nombre de sommets et E le nombre d'arêtes du graphe. En effet, chaque sommet est visité une fois et chaque arête est examinée une fois.

La complexité spatiale est également O(V) car on doit stocker les sommets visités et la file d'attente.

## Le DFS [dfs](./algos/dfs.py)
1. Execution
```bash
python main.py dfs
```
2. Temps d'éxécution

Le DFS s'éxecute en 0.99ms avec le graphe donné

3. Compléxité

Le DFS a une complexité temporelle de O(V + E) où V est le nombre de sommets et E le nombre d'arêtes du graphe. En effet, chaque sommet est visité une fois et chaque arête est examinée une fois.
La complexité spatiale est O(V) car on doit stocker les sommets visités et la pile d'appels récursive.

## BFS avec détection des composantes connexes [bfs connexe](./algos/bfs.py)
```bash
python main.py bfs-connexe 
```

## DFS avec détéction de cycle [dfs cycle](./algos/dfs.py)
```bash
python main.py dfs_cycle
```
## Préférence du DFS ou du BFS

# Exercice 2 : Algorithmes de Dijkstra

1. Ecriture du pseudo code
```
Entrée :
    - G : graphe avec sommets et arêtes pondérées
    - S : sommet de départ

Initialisation :
    Pour chaque sommet v dans G :
        distance[v] ← ∞
    distance[S] ← 0

    file_priorité ← file vide (ex: tas binaire)
    insérer (0, S) dans file_priorité   // (distance, sommet)

    visité ← ensemble vide

Tant que file_priorité n’est pas vide :
    (d, u) ← extraire_min(file_priorité)

    Si u ∈ visité :
        continuer

    ajouter u à visité

    Pour chaque voisin v de u :
        poids ← poids de l’arête (u, v)

        Si distance[u] + poids < distance[v] :
            distance[v] ← distance[u] + poids
            insérer (distance[v], v) dans file_priorité

Retourner distance

```

2. Implémentation de l'algorithme [dijkstra](./algos/dijkstra.py)
```bash
python main.py dijkstra
```

3. Résolution du problème du plus court chemin

En appliquant l’algorithme de Dijkstra depuis le sommet A, on obtient les distances minimales suivantes vers les autres sommets :
- A → B : 4
- A → C : 2
- A → D : 9
- A → E : 5
- A → F : 15
Ces résultats représentent les plus courts chemins en termes de coût total (somme des poids).

4. Analyse de la complexité

L'algorithme de Dijkstra a une complexité temporelle de O((V + E) * log(V)) où V est le nombre de sommets et E le nombre d'arêtes du graphe.
La complexité temporelle s'explique par le fait que chaque sommet est visité une fois et chaque arête est examinée une fois. De plus, l'utilisation d'une file de priorité permet d'optimiser la recherche du sommet avec la distance minimale.

La complexité spatiale est O(V) car on doit stocker les sommets visités et la file de priorité.

# Exercice 3 : Algorithmes de Bellman-Ford