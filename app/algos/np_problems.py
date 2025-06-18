"""
Exercice 7 : Problèmes NP-complets - Version corrigée
"""

def is_satisfiable(clauses):
    """Vérificateur SAT avec affectation prédéfinie"""
    print("=== Vérification SAT ===")

    # Affectation de test
    assignment = {"A": True, "B": False, "C": True, "D": True}
    print(f"Affectation testée: {assignment}")
    print(f"Clauses: {clauses}")

    for i, clause in enumerate(clauses):
        satisfied = False
        print(f"\nClause {i+1}: {clause}")

        for literal in clause:
            var = literal.strip("¬")
            is_negated = literal.startswith("¬")

            var_value = assignment.get(var, False)
            literal_value = not var_value if is_negated else var_value

            print(f"  {literal}: {var}={var_value} → {literal_value}")

            if literal_value:
                satisfied = True
                print(f"  ✓ Clause satisfaite par {literal}")
                break

        if not satisfied:
            print(f"  ✗ Clause {i+1} non satisfaite")
            return False

    print("\n✓ Toutes les clauses sont satisfaites!")
    return True

def tsp_nearest_neighbor(matrix):
    """Heuristique TSP du plus proche voisin"""
    print("=== Problème du Voyageur de Commerce (TSP) ===")

    n = len(matrix)
    print(f"Nombre de villes: {n}")

    # Affichage de la matrice
    print("\nMatrice des distances:")
    for i in range(n):
        print(f"Ville {i}: {matrix[i]}")

    visited = [False] * n
    path = [0]  # Commencer par la ville 0
    visited[0] = True
    total_cost = 0

    print(f"\nDépart depuis la ville 0")

    # Algorithme du plus proche voisin
    for step in range(n - 1):
        current_city = path[-1]
        min_distance = float('inf')
        next_city = -1

        # Trouver la ville la plus proche non visitée
        for city in range(n):
            if not visited[city] and matrix[current_city][city] < min_distance:
                min_distance = matrix[current_city][city]
                next_city = city

        # Aller à la ville la plus proche
        path.append(next_city)
        visited[next_city] = True
        total_cost += min_distance

        print(f"Étape {step + 1}: Ville {current_city} → Ville {next_city} (distance: {min_distance})")

    # Retourner au point de départ
    return_cost = matrix[path[-1]][0]
    total_cost += return_cost
    path.append(0)

    print(f"Retour: Ville {path[-2]} → Ville 0 (distance: {return_cost})")
    print(f"\nChemin final: {' → '.join(map(str, path))}")
    print(f"Coût total: {total_cost}")

    return path, total_cost