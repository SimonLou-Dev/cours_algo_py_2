# TP1 - S2 d'Algorithmique : Algorithmes de Graphes & Structures de Données

## 📦 Installation

1. Clone ce dépôt :
```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet
```

# Configuration du json

```json
{
  "matrice_start": "",
  "matrice": {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "E": 3},
    "D": {"B": 5, "F": 6},
    "E": {"C": 3},
    "F": {"D": 6}
  }
}
```

`matrice_start` : sommet de départ pour le parcours du graphe
`matrice` : représentation du graphe sous forme de dictionnaire où chaque clé est un sommet et la valeur est un dictionnaire des voisins avec les poids des arêtes.

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

TODO

# Exercice 2 : Algorithme de Dijkstra

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

NB: la comparaise avec bellman ford et fair dans le 6. de la partie [Bellman-Ford](#exercice-3--algorithme-de-bellman-ford)

4. Analyse de la complexité

L'algorithme de Dijkstra a une complexité temporelle de O((V + E) * log(V)) où V est le nombre de sommets et E le nombre d'arêtes du graphe.
La complexité temporelle s'explique par le fait que chaque sommet est visité une fois et chaque arête est examinée une fois. De plus, l'utilisation d'une file de priorité permet d'optimiser la recherche du sommet avec la distance minimale.

La complexité spatiale est O(V) car on doit stocker les sommets visités et la file de priorité.

# Exercice 3 : Algorithme de Bellman-Ford


1. Pseudo code pour de Bellman-Ford

```
Entrée :
    - G : graphe avec sommets et arêtes pondérées
    - S : sommet de départ

Initialisation :
    Pour chaque sommet v dans G :
        distance[v] ← ∞
    distance[S] ← 0

    Pour i allant de 0 à nombre de sommet du graph - 1 : 
        Pour chaque sommet V dans G :
            Pour chaque voisin N de V :
                W <- poids entre V et N
                Si dinstance[V] + poid < distance[N] alors
                    distance[N] <- distance[V] + W
                fin Si
            Fin pour chaque
        Fin pour chaque
    Fin pour chaque

    # Détection des cycle négatif
    Pour chaque sommet V dans G :
         Pour chaque voisin N de V :
            W <- poids entre V et N
            # S'il est encore possible d'améliorer les distance, alors le graph contuent un cycle négatif
            Si distance[V] + W < distance[N] alors
                renvoyer "Le graph à un cycle négatif"
            Fin si
        fin pour chaque
    Fin pour chaque
    # Fin de la détection de cycle négatif

retourner distance
```

2. Implémentation et test de l'algorithme [bellman-ford](./algos/bellman-ford.py)
```bash
python main.py bf
```

3. Détection des cycles négatif

La détection des cycles négatif se fait grâce à la boucle suivante dans le pseudo-code
```
# Détection des cycle négatif
    Pour chaque sommet V dans G :
         Pour chaque voisin N de V :
            W <- poids entre V et N
            # S'il est encore possible d'améliorer les distance, alors le graph contuent un cycle négatif
            Si distance[V] + W < distance[N] alors
                renvoyer "Le graph à un cycle négatif"
            Fin si
        fin pour chaque
    Fin pour chaque
    # Fin de la détection de cycle négatif
```

Comment cela fonctionne ?
> Gràce à l'instruction `Pour i allant de 0 à nombre de sommet du graph - 1` dans le pseudo-code, les distance minimal vont se propager jusqu'à sommets les plus loins. Si il est encore possible d'améliorer ce résultat alors que toutes les distances ont été propagées au plus loins, alors le graph contient un cycle négatif.

Lancement du code

```bash
python main.py bf-neg
```

4. Les cycles négatif dans la pratique
Les cycles négatif ne peuvent pas s'appliquer dans les réseaux informatique car les distances ou les couts sont physique donc par définition toujours positifs.

Dans un jeu vidéo, un cycle négatif peut représenter une boucle d’actions où le joueur gagne constamment des points ou des ressources, ce qui casse l’équilibre du jeu.
> Exemple : Dans un RPG, un joueur découvre qu’il peut acheter une potion pour 5 pièces d’or, la revendre pour 6 pièces dans une autre ville, puis revenir — en boucle — gagnant 1 pièce à chaque cycle sans fin. Ce cycle économique "achete → voyage → revend → revient" correspond à un cycle négatif de coût qui exploite une faille dans l'équilibrage du jeux.

5. Analyse de complexité

La complexité temporelle de Bellman-Ford est O(VE), car on parcourt toutes les arêtes E pendant V - 1 itérations (où V est le nombre de sommets). Cela donne une complexité de O((V - 1) * E), et comme le -E est négligeable face à VE, on retient O(VE).

La complexité spatiale est O(V), car on stocke uniquement un tableau (ou dictionnaire) de distances pour chaque sommet.

6. Comparaison avec Dijkstra

L’algorithme de Bellman-Ford permet de calculer les plus courts chemins depuis un sommet, même en présence de poids négatifs, et peut détecter les cycles de poids négatif. En revanche, il est plus lent avec une complexité en temps de O(VE). L’algorithme de Dijkstra est plus rapide (O((V + E) log V)) mais ne fonctionne que si tous les poids sont positifs. Dijkstra est donc souvent préféré pour les graphes classiques (réseaux, cartes), tandis que Bellman-Ford est utile pour des cas plus généraux ou complexes. Le choix dépend du type de graphe et des contraintes sur les poids.

# Exercice 4 : l'algorithmes de Ford-Fulkerson et Edmonds-Karp

1. Pseudo code Ford-Fulkerson

```
fonction BFS(source, puits, graph, parent):
    initialiser file ← [source]
    initialiser ensemble visité ← {source}
    tant que la file n’est pas vide :
        u ← retirer un sommet de la file
        pour chaque voisin v de u :
            si v non visité et capacité résiduelle (u, v) > 0 :
                file ← file + [v]
                parent[v] ← u
                ajouter v à visité
                si v == puits :
                    retourner Vrai
    retourner Faux

fonction FordFulkerson(graph, source, puits):
    initialiser parent[v] ← None pour chaque sommet v
    flot_max ← 0

    tant que BFS(source, puits) retourne Vrai :
        chemin ← chemin reconstruit depuis parent
        flot_chemin ← capacité minimale sur ce chemin
        pour chaque arête (u, v) du chemin :
            diminuer capacité de (u, v) de flot_chemin
            augmenter capacité de (v, u) de flot_chemin
        flot_max ← flot_max + flot_chemin

    retourner flot_max
```


2. Implémentation et test de l'algorithme [Ford-Fulkerson](./algos/ff.py)
```bash
python main.py ff
```

3. Analyse de la complexité de l'algorithme Ford-Fulkerson

La complexité temporelle de l’algorithme de Ford-Fulkerson dépend du nombre d’itérations nécessaires pour atteindre le flot maximal. À chaque itération, on cherche un chemin augmentant, ce qui prend O(E) dans le cas d’une recherche en profondeur (DFS), et le flot est augmenté d’au moins une unité à chaque fois. Si le flot maximum est F, la complexité temporelle est donc O(F × E).

La complexité spatiale, l’algorithme utilise un dictionnaire pour suivre les parents des sommets soit O(V).

4. Pseudo code Edmonds-Karp

```
fonction BFS(source, puits,  graph, parent):
    créer une file queue ← [source]
    créer un ensemble visité ← {source}
    tant que queue n’est pas vide :
        u ← queue.pop()
        pour chaque voisin v de u :
            si v non visité et capacité résiduelle graph[u][v] > 0 :
                parent[v] ← u
                ajouter v à queue
                ajouter v à visité
                si v = puits :
                    retourner Vrai
    retourner Faux

fonction EdmondsKarp(graph, source, puits):
    initialiser parent[v] ← None pour tout sommet v
    max_flow ← 0

    tant que BFS(source, puits) est Vrai :
        chemin ← reconstruit depuis parent[]
        path_flow ← +∞
        s ← puits
        tant que s ≠ source :
            path_flow ← min(path_flow, graph[parent[s]][s])
            s ← parent[s]
        max_flow ← max_flow + path_flow

        mettre à jour les capacités résiduelles :
        v ← puits
        tant que v ≠ source :
            u ← parent[v]
            graph[u][v] ← graph[u][v] - path_flow
            graph[v][u] ← graph[v][u] + path_flow
            v ← parent[v]

    retourner max_flow
```

5. Implémentation et test de l'algorithme [Edmonds-Karp](./algos/ek.py)

6. Analyse de la complexité de l'algorithme Edmonds-Karp

L’algorithme d’Edmonds-Karp a une complexité temporelle de O(V × E²), où V est le nombre de sommets et E le nombre d’arêtes. Cette complexité vient du fait qu’il utilise une recherche en largeur (BFS) pour trouver les chemins augmentants les plus courts, ce qui prend O(E) par itération, et qu’il peut y avoir au plus O(V × E) itérations. 

Du côté mémoire, il utilise O(E) d’espace pour stocker le tableau les parents.

7. Discuter des cas où Edmonds-Karp est préférable à Ford-Fulkerson.

L’algorithme d’Edmonds-Karp est préférable à Ford-Fulkerson dans les cas où l’on souhaite garantir une terminaison plus rapide, notamment lorsque les capacités des arêtes sont grandes. En effet, Ford-Fulkerson simple peut effectuer un très grand nombre d’itérations si le flot est incrémenté par de très petites quantités (par exemple 1 unité à la fois sur des capacités très grandes), ce qui peut rendre sa complexité exponentielle dans le pire cas. Edmonds-Karp, en utilisant une recherche en largeur (BFS) pour toujours choisir le chemin augmentant le plus court (en nombre d’arêtes), évite ce problème et garantit une complexité polynomiale (O(V × E²)). Il est donc particulièrement adapté aux grands graphes ou aux applications critiques (comme les réseaux de transport ou de communication) où la performance prévisible est essentielle.
