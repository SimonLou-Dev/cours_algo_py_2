def bellman_ford(graph: dict[str, dict[str, int]], start: str) -> dict[str, int]:
    """L'algorithme de Bellman Ford est un algorithme de recherche informée.

    Il trouve le plus court chemin entre un sommet de départ et tous les autres sommets du graph.
    Il supporte les arrêtes de poids négatif.

    Args:
        graph (dict[str, dict[str, int]]): Le graph.

        start (str): Le sommet de départ.

    Returns:
        dict[str, int]: Les distances minimales depuis le sommet de départ.

    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor in graph[vertex]:
                poids = graph[vertex][neighbor]
                if (current_weight := distances[vertex] + poids) < distances[neighbor]:
                    distances[neighbor] = current_weight

    return distances
def bellman_ford_contains_neg(start: str, graph: dict[str, dict[str, int]]) -> bool:
    """Après l'éxecution de Bellman Ford.

    Permet de trouver si le graph contient des cycles de poids négatif.

    Args:
        start (str): Le sommet de départ

        graph (dict[str, dict[str, int]]): Le graph

    Returns:
        bool: vrai, si le graphe contient un cycle négatif.

    """
    distances: dict[str, int] = bellman_ford(graph, start)

    for vertex in graph:
        for neighbor, poids in graph[vertex].items():
            if  distances[vertex] + poids < distances[neighbor]:
                return True
    return False
