"""
Exercice 7 : Problèmes NP-complets
"""

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        satisfied = False
        for literal in clause:
            var = literal.strip("¬")
            if (literal.startswith("¬") and not assignment.get(var, False)) or                (not literal.startswith("¬") and assignment.get(var, False)):
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def tsp_nearest_neighbor(matrix):
    n = len(matrix)
    visited = [False] * n
    path = [0]
    visited[0] = True
    cost = 0

    for _ in range(n - 1):
        last = path[-1]
        next_city = min((matrix[last][j], j) for j in range(n) if not visited[j])[1]
        path.append(next_city)
        visited[next_city] = True
        cost += matrix[last][next_city]

    cost += matrix[path[-1]][0]
    path.append(0)
    return path, cost
