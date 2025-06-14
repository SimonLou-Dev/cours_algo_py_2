

def run(graph: dict[str, list], start: str, visited: set = None) -> list:
    """Le DFS (Depth-First Search) est un algorithme de recherche non informée qui explore

    Args:
        graph (dict[str, list]): Le graph
        start (str): Le sommet de départ
        visited (set, optional): Les sommets déjà visités. Defaults to None.

    Returns:
        visited: Le parcours du DFS
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visiting {start}")
    for node in graph[start]:
        if node not in visited:
            run(graph, node, visited)
    return visited

def run_cyles(graph: dict[str, list], start: str, visited: set = None, parent: str = None) -> bool:
    """Version du DFS qui permet de détecter les cycles dans le graph.

    Args:
        graph (dict[str, list]): Le graph
        start (str): Le sommet de départ
        visited (set, optional): Les sommets déjà visités. Defaults to None.
        parent (str, optional): Le parent du sommet actuel. Defaults to None.

    Returns:
        visited: Le parcours du DFS
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"Visiting {start}")
    for neighbor in graph[start]:
        if neighbor not in visited:
            if run_cyles(graph, neighbor, visited, start):
                return True
        elif neighbor != parent:
            print(f"Cycle detected via {neighbor} (from {start})")
            return True
    return False

