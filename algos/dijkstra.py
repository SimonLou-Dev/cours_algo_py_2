


""""Pseudo code dijkstra:

Entrée :
    - Graphe G avec des sommets et des arêtes pondérées
    - Sommet de départ S

Initialisation :
    - Pour tous les sommets mettre une distance infinie
    - Distrance du départ à 0
    - file_priorité ← ensemble vide (ou min-heap)
    - file_priorité ← insérer (0, S)  // (distance, sommet)
    - visité ← ensemble vide

Tant que la file_priorité n’est pas vide :
    - (d, u) ← extraire le sommet avec la plus petite distance
    - Si u est déjà dans visité : continuer
    - Marquer u comme visité

    Pour chaque voisin v de u :
        - poids ← poids de l’arête (u, v)
        - Si distance[u] + poids < distance[v] :
            - distance[v] ← distance[u] + poids
            - insérer (distance[v], v) dans file_priorité

Retourner distance


"""


def dijkstra(graph: [str, str], start: str) -> dict[str, int]:
    """L'algorithme de Dijkstra est un algorithme de recherche informée qui trouve le plus
    court chemin entre un sommet de départ et tous les autres sommets du graph.

    Args:
        graph (dict[str, dict[str, int]]): Le graph
        start (str): Le sommet de départ

    Returns:
        dict[str, int]: Les distances minimales depuis le sommet de départ
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]  # (distance, node)

    while queue:
        current_distance, current_node = queue.pop(0)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                queue.append((distance, neighbor))
    return distances