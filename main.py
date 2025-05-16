import argparse
import json
from utils import mesurer_temps_execution


def main():
    parser = argparse.ArgumentParser(
        description="Boîte à outils de tests automatisés : Network et Web.",
    )

    subparsers = parser.add_subparsers(
        dest="mode",
        help="Mode de fonctionnement : network ou web",
    )

    subparsers.add_parser("dfs", help="Lancer un DFS")
    subparsers.add_parser(
        "dfs-cycle", help="Lancer un DFS qui détecte les cycles")
    subparsers.add_parser("bfs", help="Lancer un BFS")
    subparsers.add_parser(
        "bfs-connexe", help="Lancer un BFS qui permet de trouver les sommets connexes")
    subparsers.add_parser("dijkstra", help="Lancer Dijkstra")
    subparsers.add_parser("bf", help="Lancer Bellman-Ford")
    subparsers.add_parser(
        "bf-neg", help="Lancer Bellman-Ford avec détection des cyles négatifs")
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
            from algos.dfs import run as dfs
            rslt, time = mesurer_temps_execution(
                dfs, data["matrices"], data["matrice_start"])
        case "dfs-cycle":
            print("Lancement du DFS avec détection de cycles")
            from algos.dfs import run_cyles as dfs_cycle
            rslt, time = mesurer_temps_execution(
                dfs_cycle, data["matrices"], data["matrice_start"])
        case "bfs":
            print("Lancement du BFS")
            from algos.bfs import run as bfs
            rslt, time = mesurer_temps_execution(
                bfs, data["matrices"], data["matrice_start"])
        case "bfs-connexe":
            print("Lancement du BFS avec détection de connexité")
            from algos.bfs import run_find_connexe as bfs_connexe
            rslt, time = mesurer_temps_execution(bfs_connexe, data["matrices"])
        case "dijkstra":
            print("Lancement de Dijkstra")
            from algos.dijkstra import dijkstra as dijkstra
            rslt, time = mesurer_temps_execution(
                dijkstra, data["matrices"], data["matrice_start"])
        case "bf":
            print("Lancement de Bellman-Ford")
            # Lancer le module Bellman-Ford
            from algos.bellman_ford import bellman_ford
            rslt, time = mesurer_temps_execution(
                bellman_ford, data["matrices"], data["matrice_start"])
        case "bf-neg":
            print("Lancement de Floyd-Warshall")
            from algos.bellman_ford import bellman_ford, bellman_ford_contains_neg
            rslt1, time1 = mesurer_temps_execution(
                bellman_ford, data["matrices"], data["matrice_start"])
            rslt2, time2 = mesurer_temps_execution(
                bellman_ford_contains_neg, rslt1, data["matrices"])
            time = time1 + time2

            rslt = {
                "Résultat de Bellman-Forst": rslt1,
                "Contient un cycle de poid négatif": rslt2
            }

        case "ff":
            print("Lancement de Floyd-Warshall")
            from algos.ff import ford_fulkerson
            rslt, time = mesurer_temps_execution(
                ford_fulkerson, data["matrices"], data["matrice_start"], data["matrice_end"])
        case "ek":
            print("Lancement d'Edmonds-Karp")
            # Lancer le module Edmonds-Karp
            from algos.ek import edmonds_karp
            rslt, time = mesurer_temps_execution(
                edmonds_karp, data["matrices"], data["matrice_start"], data["matrice_end"])
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

    # ============== Fin du switch ==============

    print("Résultat :")
    print(rslt)
    print(f"Temps d'exécution : {time} ms")

    # ============== Fin du programme ==============


if __name__ == '__main__':
    main()
