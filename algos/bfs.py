

def run(graph: dict[str, list], start: str) -> list:
    """Le BFS (Breadth-First Search) est un algorithme de recherche non informée qui explore
    le graph en largeur. Il visite tous les sommets d'un niveau avant de passer au suivant.

    Args:
        graph (dict[str, list]): Le graph
        start (str): Le sommet de départ

    Returns:
        visited: Le parcours du BFS
    """
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(f"Visiting {node}")
            visited.add(node)
            queue.extend(graph[node])
    return visited


def run_find_connexe(graph: dict[str, list]) -> list[list[str]]:
    all_visited = set()
    components = []

    for node in graph:
        if node not in all_visited:
            print(f"\nNouvelle composante depuis {node}")
            visited = run(graph, node)
            components.append(list(visited))
            all_visited.update(visited)
    return components


def bfs_boolean(graph: dict[str, list], parent: dict, source: str, sink: str) -> bool:
    """Permet de faire tourner le BFS pour aller d'un point A à un point B, utilisé par des algo plus complexe.

    Args:
        graph (dict[str, list]): Le graph
        source (str): Le sommet de départ
        sink (str): sommet d'arrivé
        parent dict[str, list[str]]: liste des parents d'un sommet

    Return:
        bool: Renvoi True s'il existe un chemin entre source et sink
    """
    visited = set()
    queue = [source]
    while queue:
        current_vertex = queue.pop(0)
        for vertex in graph[current_vertex]:
            if vertex not in visited and graph[current_vertex][vertex] > 0:
                queue.append(vertex)
                visited.add(vertex)
                parent[vertex] = current_vertex
                if vertex == sink:
                    return True
    return False
