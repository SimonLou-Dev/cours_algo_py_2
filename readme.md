# TP1 - S2 d'Algorithmique : Algorithmes de Graphes & Structures de Données

## 📦 Installation

1. Clone ce dépôt :
```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet
```

# Exercice 1 : Recherche et Parcours de Graphes
## Le BFS [bfs](./algos/bfs.py)
1. Execution
```bash
python main.py bfs
```
2. Temps d'éxécution

3. Compléxité

## Le DFS [dfs](./algos/dfs.py)
1. Execution
```bash
python main.py dfs
```
2. Temps d'éxécution

3. Compléxité


## BFS avec détection des composantes connexes [bfs connexe](./algos/bfs.py)
```bash
python main.py bfs-connexe 
```
2. Temps d'éxécution

3. Compléxité


## DFS avec détéction de cycle [dfs cycle](./algos/dfs.py)
```bash
python main.py dfs_cycle
```

2. Temps d'éxécution

3. Compléxité


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

4. Analyse de la complexité

