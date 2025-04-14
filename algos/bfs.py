

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