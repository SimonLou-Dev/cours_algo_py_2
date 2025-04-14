import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Boîte à outils de tests automatisés : Network et Web.",
    )

    subparsers = parser.add_subparsers(
        dest="mode",
        help="Mode de fonctionnement : network ou web",
    )

    subparsers.add_parser("dfs", help="Lancer un DFS")
    subparsers.add_parser("dfs-cycle", help="Lancer un DFS qui détecte les cycles")
    subparsers.add_parser("bfs", help="Lancer un BFS")
    subparsers.add_parser("bfs-connexe", help="Lancer un BFS qui permet de trouver les sommets connexes")
    subparsers.add_parser("dijkstra", help="Lancer Dijkstra")
    subparsers.add_parser("bf", help="Lancer Bellman-Ford")
    subparsers.add_parser("ff", help="Lancer Floyd-Warshall")
    subparsers.add_parser("ek", help="Lancer Edmonds-Karp")
    subparsers.add_parser("rand", help="Tri random")
    subparsers.add_parser("avl", help="Arbre AVL")
    subparsers.add_parser("np", help="Problèmes NP")

    # ============== Parsing ==============
    args = parser.parse_args()

    # ============== Gestion des erreurs ==============
    if args.mode is None:
        parser.print_help()
        exit(1)

    # ============== Lecture du fichier ==============
    with open("source.json", "r") as f:
        data = json.loads(f.read())
        f.close()

    # ============== Lancement des modules ==============
    match args.mode:
        case "dfs":
            print("Lancement du DFS")
            # Lancer le module DFS
            from algos.dfs import run as dfs
            dfs_rslt = dfs(data["matrices"], data["matrice_start"])
            print(f"Résultat du DFS : {dfs_rslt}")
        case "dfs-cycle":
            print("Lancement du DFS avec détection de cycles")
            # Lancer le module DFS avec détection de cycles
            from algos.dfs import run_cyles as dfs_cycle
            dfs_cycle_rslt = dfs_cycle(data["matrices"], data["matrice_start"])
            print(f"Résultat du DFS avec détection de cycles : {dfs_cycle_rslt}")
        case "bfs":
            print("Lancement du BFS")
            # Lancer le module BFS
            from algos.bfs import run as bfs
            bfs_rslt = bfs(data["matrices"], data["matrice_start"])
            print(f"Résultat du BFS : {bfs_rslt}")
        case "bfs-connexe":
            print("Lancement du BFS avec détection de connexité")
            # Lancer le module BFS avec détection de connexité
            from algos.bfs import run_find_connexe as bfs_connexe
            bfs_connexe_rslt = bfs_connexe(data["matrices"])
            print(f"Résultat du BFS avec détection de connexité : {bfs_connexe_rslt}")
        case "dijkstra":
            print("Lancement de Dijkstra")
            # Lancer le module Dijkstra
            from algos.dijkstra import dijkstra as dijkstra
            dijkstra_rslt = dijkstra(data["matrices"], data["matrice_start"])
            print(f"Résultat de Dijkstra : {dijkstra_rslt}")
        case "bf":
            print("Lancement de Bellman-Ford")
            # Lancer le module Bellman-Ford
        case "ff":
            print("Lancement de Floyd-Warshall")
            # Lancer le module Floyd-Warshall
        case "ek":
            print("Lancement d'Edmonds-Karp")
            # Lancer le module Edmonds-Karp
        case "rand":
            print("Lancement du tri random")
            # Lancer le module de tri random
        case "avl":
            print("Lancement de l'arbre AVL")
            # Lancer le module d'arbre AVL
        case "np":
            print("Lancement des problèmes NP")
            # Lancer le module de problèmes NP
        case _:
            print("Mode non reconnu")
            parser.print_help()
            exit(1)




if __name__ == '__main__':
    main()