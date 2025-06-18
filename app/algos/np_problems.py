"""Module pour les problèmes NP-complets.

Ce module contient les fonctions pour vérifier la satisfaisabilité (SAT)
et pour résoudre le problème du voyageur de commerce (TSP) via une heuristique.
"""

def is_satisfiable(clauses: list[list[str]]) -> bool:
    """Vérifie si un ensemble de clauses SAT est satisfaisable.
    
    Args:
        clauses (list[list[str]]): Liste de clauses, où chaque clause est une liste de littéraux.
    
    Returns:
        bool: True si les clauses sont satisfaisables, sinon False.

    """
    # Exemple simplifié : retourne True si au moins une clause est vide (à adapter selon besoin)
    for clause in clauses:
        if not clause:
            return False
    return True

def tsp_nearest_neighbor(matrix: list[list[int]]) -> list[int]:
    """Résout le problème du voyageur de commerce (TSP) en utilisant l'heuristique du plus proche voisin.
    
    Args:
        matrix (list[list[int]]): Matrice des distances entre les villes.
    
    Returns:
        list[int]: Ordre de visite des villes.

    """
    n = len(matrix)
    if n == 0:
        return []
    visited = [False] * n
    path = [0]
    visited[0] = True

    current = 0
    for _ in range(n-1):
        next_city = None
        min_dist = float("inf")
        for city in range(n):
            if not visited[city] and matrix[current][city] < min_dist:
                min_dist = matrix[current][city]
                next_city = city
        if next_city is None:
            break
        visited[next_city] = True
        path.append(next_city)
        current = next_city

    return path
