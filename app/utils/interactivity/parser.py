"""Command line argument parser for the algorithm toolbox."""

import argparse
from typing import Any

from app.exercises import ExerciseManager


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.
    
    Returns:
        Configured ArgumentParser instance with all subcommands.

    """
    parser = argparse.ArgumentParser(
        description="Boîte à outils d'algorithmes de graphes et structures de données",
        prog="python -m app.main",
    )

    # Add debug flag
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Activer le mode debug avec logs détaillés",
    )

    # Create subparsers for different algorithms
    subparsers = parser.add_subparsers(
        dest="mode",
        help="Algorithme à exécuter",
        metavar="ALGORITHM",
    )

    # Add all algorithms from enum dynamically
    for algo in ExerciseManager.get_all_algorithms():
        info = ExerciseManager.get_algorithm_info(algo)

        # Create subparser for each algorithm
        algo_parser = subparsers.add_parser(
            info.command,
            help=info.description,
        )

        # Add additional help text showing the exercise
        algo_parser.description = f"{info.description}\n\nExercice: {info.exercise}"

        # You can add algorithm-specific arguments here if needed
        # For example:
        # if info.needs_start:
        #     algo_parser.add_argument("--start", type=int, help="Sommet de départ")
        # if info.needs_end:
        #     algo_parser.add_argument("--end", type=int, help="Sommet d'arrivée")

    return parser


def parse_args() -> Any:
    """Parse command line arguments.
    
    Returns:
        Parsed arguments namespace.

    """
    parser = create_parser()
    return parser.parse_args()


def print_algorithm_help(command: str) -> None:
    """Print detailed help for a specific algorithm."""
    algo_type = ExerciseManager.get_by_command(command)
    if not algo_type:
        print(f"Algorithme '{command}' non trouvé")
        return

    info = ExerciseManager.get_algorithm_info(algo_type)

    print(f"\n=== {info.name} ===")
    print(f"Commande: {info.command}")
    print(f"Catégorie: {info.category}")
    print(f"Description: {info.description}")
    print(f"Exercice: {info.exercise}")

    # Remove the needs_start/needs_end references and replace with parameters
    if info.parameters:
        params_str = ", ".join(info.parameters)
        print(f"Paramètres: {params_str}")

    function_status = "✓ Implémenté" if ExerciseManager.get_algorithm_function(algo_type) else "✗ Non implémenté"
    print(f"État: {function_status}")


def list_all_algorithms() -> None:
    """Print a list of all available algorithms organized by category."""
    categories = ExerciseManager.get_by_category()

    print("\n=== ALGORITHMES DISPONIBLES ===\n")

    for category, algos in categories.items():
        print(f"📁 {category}")
        print("-" * (len(category) + 3))

        for algo in algos:
            info = ExerciseManager.get_algorithm_info(algo)
            status = "✓" if ExerciseManager.get_algorithm_function(algo) else "✗"
            print(f"  {status} {info.command:<15} - {info.name}")

        print()  # Empty line between categories

    print("Utilisation:")
    print("  python -m app.main                    # Mode interactif")
    print("  python -m app.main <command>          # Exécution directe")
    print("  python -m app.main --debug <command>  # Avec logs debug")
