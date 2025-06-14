"""Exercise definitions and algorithm metadata for the toolbox."""

from enum import Enum
from typing import Any, Callable, Dict, List, NamedTuple, Tuple


class AlgorithmInfo(NamedTuple):
    """Algorithm information container."""

    name: str
    command: str
    description: str
    exercise: str
    category: str
    function: Callable[..., Any]
    parameters: tuple[str, ...] = ()


class AlgorithmType(Enum):
    """Enumeration of all available algorithms with their metadata."""

    # Graph Algorithms (matrice, matrice_start)
    DFS = AlgorithmInfo(
        name="DFS (Depth-First Search)",
        command="dfs",
        description="Parcours en profondeur d'un graphe",
        exercise="Implémenter un parcours DFS et afficher l'ordre de visite des sommets",
        category="Parcours de Graphes",
        function=lambda: __import__("app.algos.dfs", fromlist=["run"]).run,
        parameters=("matrices", "matrice_start"),
    )

    DFS_CYCLE = AlgorithmInfo(
        name="DFS + Détection de Cycles",
        command="dfs-cycle",
        description="DFS avec détection de cycles dans le graphe",
        exercise="Utiliser DFS pour détecter la présence de cycles dans un graphe orienté",
        category="Parcours de Graphes",
        function=lambda: __import__("app.algos.dfs", fromlist=["run_cyles"]).run_cyles,
        parameters=("matrices", "matrice_start"),
    )

    BFS = AlgorithmInfo(
        name="BFS (Breadth-First Search)",
        command="bfs",
        description="Parcours en largeur d'un graphe",
        exercise="Implémenter un parcours BFS et calculer les distances depuis un sommet source",
        category="Parcours de Graphes",
        function=lambda: __import__("app.algos.bfs", fromlist=["run"]).run,
        parameters=("matrices", "matrice_start"),
    )

    BFS_CONNEXE = AlgorithmInfo(
        name="BFS Composantes Connexes",
        command="bfs-connexe",
        description="Trouver les composantes connexes avec BFS",
        exercise="Utiliser BFS pour identifier toutes les composantes connexes d'un graphe",
        category="Parcours de Graphes",
        function=lambda: __import__("app.algos.bfs", fromlist=["run_find_connexe"]).run_find_connexe,
        parameters=("matrices",),
    )

    DIJKSTRA = AlgorithmInfo(
        name="Algorithme de Dijkstra",
        command="dijkstra",
        description="Plus court chemin avec poids positifs",
        exercise="Calculer les plus courts chemins depuis un sommet source (poids ≥ 0)",
        category="Plus Courts Chemins",
        function=lambda: __import__("app.algos.dijkstra", fromlist=["dijkstra"]).dijkstra,
        parameters=("matrices", "matrice_start"),
    )

    BELLMAN_FORD = AlgorithmInfo(
        name="Algorithme de Bellman-Ford",
        command="bf",
        description="Plus court chemin avec poids négatifs autorisés",
        exercise="Calculer les plus courts chemins même avec des arêtes de poids négatif",
        category="Plus Courts Chemins",
        function=lambda: __import__("app.algos.bellman_ford", fromlist=["bellman_ford"]).bellman_ford,
        parameters=("matrices", "matrice_start"),
    )

    BELLMAN_FORD_NEG = AlgorithmInfo(
        name="Bellman-Ford + Cycles Négatifs",
        command="bf-neg",
        description="Bellman-Ford avec détection de cycles négatifs",
        exercise="Détecter les cycles de poids négatif dans un graphe pondéré",
        category="Plus Courts Chemins",
        function=lambda: __import__("app.algos.bellman_ford", fromlist=["bellman_ford_contains_neg"]).bellman_ford_contains_neg,
        parameters=("matrice_start", "matrices"),  # Note: different order for this function
    )

    # Flow Algorithms (matrice, matrice_start, matrice_end)
    FORD_FULKERSON = AlgorithmInfo(
        name="Ford-Fulkerson",
        command="ff",
        description="Calcul du flot maximum dans un réseau",
        exercise="Trouver le flot maximum entre une source et un puits",
        category="Flots Maximum",
        function=lambda: __import__("app.algos.ff", fromlist=["ford_fulkerson"]).ford_fulkerson,
        parameters=("matrices", "matrice_start", "matrice_end"),
    )

    EDMONDS_KARP = AlgorithmInfo(
        name="Edmonds-Karp",
        command="ek",
        description="Ford-Fulkerson optimisé avec BFS",
        exercise="Version optimisée de Ford-Fulkerson utilisant BFS pour les chemins augmentants",
        category="Flots Maximum",
        function=lambda: __import__("app.algos.ek", fromlist=["edmonds_karp"]).edmonds_karp,
        parameters=("matrices", "matrice_start", "matrice_end"),
    )

    # List Algorithms (list)
    RANDOM_SORT = AlgorithmInfo(
        name="Tri Rapide Randomisé",
        command="rand",
        description="Tri rapide avec pivot randomisé",
        exercise="Exercice 5 : Tri Rapide Randomisé",
        category="Algorithmes de Tri",
        function=lambda: None,
        parameters=("rand_list",),
    )

    RANDOM_COMPARE = AlgorithmInfo(
        name="Comparaison Tris",
        command="rand-compare",
        description="Comparaison de différents algorithmes de tri",
        exercise="Comparer les performances entre tris randomisés et tris",
        category="Algorithmes de Tri",
        function=lambda: None,
        parameters=("rand_list",),
    )

    # Tree Operations (tree, number_list)
    TREE_PUT = AlgorithmInfo(
        name="Insertion AVL",
        command="tree-put",
        description="Insertion dans un arbre AVL",
        exercise= "Implémenter l'Insertion",
        category="Structures de Données",
        function=lambda: None,
        parameters=("tree", "number_list"),
    )

    TREE_DEL = AlgorithmInfo(
        name="Suppression AVL",
        command="tree-del",
        description="Suppression dans un arbre AVL",
        exercise="Implémenter la suppression",
        category="Structures de Données",
        function=lambda: None,
        parameters=("tree", "number_list"),
    )

    # Tree Equilibrium (tree)
    TREE_EQ = AlgorithmInfo(
        name="Équilibrage AVL",
        command="tree-eq",
        description="Analyse d'équilibrage d'un arbre AVL",
        exercise="Analyser et corriger l'équilibrage d'un arbre",
        category="Structures de Données",
        function=lambda: None,
        parameters=("tree",),
    )

    # NP Problems
    NP_SAT = AlgorithmInfo(
        name="Problème SAT",
        command="np-sat",
        description="Vérificateur pour le problème SAT",
        exercise="Exercice 7 : Problème SAT",
        category="Complexité NP",
        function=lambda: None,
        parameters=("sat_clauses",),
    )

    NP_TSP = AlgorithmInfo(
        name="Problème TSP",
        command="np-tsp",
        description="Heuristique pour le voyageur de commerce",
        exercise="Implémenter une heuristique pour le TSP",
        category="Complexité NP",
        function=lambda: None,
        parameters=("tsp_matrix",),
    )





class ExerciseManager:
    """Manager for exercise information and categorization."""

    @staticmethod
    def get_all_algorithms() -> List[AlgorithmType]:
        """Get all available algorithms."""
        return list(AlgorithmType)

    @staticmethod
    def get_by_command(command: str) -> AlgorithmType | None:
        """Get algorithm by command string."""
        for algo in AlgorithmType:
            if algo.value.command == command:
                return algo
        return None

    @staticmethod
    def get_by_category() -> Dict[str, List[AlgorithmType]]:
        """Get algorithms grouped by category."""
        categories: Dict[str, List[AlgorithmType]] = {}

        for algo in AlgorithmType:
            category = algo.value.category
            if category not in categories:
                categories[category] = []
            categories[category].append(algo)

        return categories

    @staticmethod
    def get_all_commands() -> List[str]:
        """Get all valid command strings."""
        return [algo.value.command for algo in AlgorithmType]

    @staticmethod
    def get_algorithm_info(algo_type: AlgorithmType) -> AlgorithmInfo:
        """Get detailed information for an algorithm."""
        return algo_type.value

    @staticmethod
    def get_algorithm_function(algo_type: AlgorithmType) -> Callable[..., Any] | None:
        """Get the function associated with an algorithm."""
        info = algo_type.value

        # Try to get the function
        try:
            return info.function()
        except (ImportError, AttributeError):
            return None

    @staticmethod
    def is_algorithm_available(algo_type: AlgorithmType) -> bool:
        """Check if an algorithm is available for execution."""
        return ExerciseManager.get_algorithm_function(algo_type) is not None

    @staticmethod
    def execute_algorithm(algo_type: AlgorithmType, data: Dict[str, Any]) -> Tuple[Any, float]:
        """Execute an algorithm with appropriate parameters."""
        from app.utils.exec_time import mesurer_temps_execution

        info = algo_type.value
        algorithm_func = ExerciseManager.get_algorithm_function(algo_type)

        if algorithm_func is None:
            raise ValueError(f"Algorithme '{info.name}' non disponible")

        # Check if it's a placeholder function (returns a string)
        if isinstance(algorithm_func, str) or (hasattr(algorithm_func, '__name__') and algorithm_func.__name__ == "_placeholder_function"):
            return algorithm_func, 0.0

        # Prepare parameters
        args = ExerciseManager._prepare_parameters(info.parameters, data)

        # Execute with timing
        return mesurer_temps_execution(algorithm_func, *args)

    @staticmethod
    def _prepare_parameters(param_names: tuple[str, ...], data: Dict[str, Any]) -> List[Any]:
        """Prepare parameters based on parameter names."""
        args = []

        for param_name in param_names:
            match param_name:
                case "matrices":
                    args.append(data["matrices"])
                case "matrice_start":
                    args.append(data["matrice_start"])
                case "matrice_end":
                    args.append(data["matrice_end"])
                case "rand_list":
                    args.append(data.get("rand_list", [10, 7, 8, 9, 1, 5]))
                case "tree":
                    args.append(data.get("tree", {}))
                case "number_list":
                    args.append(data.get("number_list", [10, 20, 30, 40, 50, 25]))
                case "sat_clauses":
                    args.append(data.get("sat_clauses", []))
                case "tsp_matrix":
                    args.append(data.get("tsp_matrix", []))
                case _:
                    args.append(data.get(param_name))

        return args
