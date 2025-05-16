def bellman_ford(graph: [str, str], start: str) -> dict[str, int]:
    """L'algorithme de Bellman Ford est un algorithme de recherche informée qui trouve le plus
    court chemin entre un sommet de départ et tous les autres sommets du graph, il supporte le arrètes de poid négatif.

    Args:
        graph (dict[str, dict[str, int]]): Le graph
        start (str): Le sommet de départ

    Returns:
        dict[str, int]: Les distances minimales depuis le sommet de départ
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, poids in graph[vertex].items():
                if (current_weight := distances[vertex] + poids) < distances[neighbor]:
                    distances[neighbor] = current_weight
                
    return distances

def bellman_ford_contains_neg(distances: dict[str, int], graph: [str, str]) -> bool:
    """Après l'éxecution de Bellman Ford, permet de trouver si le graph contient des cycles de poids négatif.

    Args:
        distances (dict[str, int]) : résultat de Bellman-Ford
        graph (dict[str, dict[str, int]]): Le graph
    
    Returns:
        bool: vrai, si le graphe contient un cycle négatif.

    """

    for vertex in graph:
        for neighbor, poids in graph[vertex].items():
            if  distances[vertex] + poids < distances[neighbor]:
                return True
    return False
