from app.algos.bfs import bfs_boolean


def ford_fulkerson(graph: dict[str, list], source: str, dest: str):
    parents = dict.fromkeys(graph)
    flot_maximum = 0

    while bfs_boolean(graph=graph, source=source, sink=dest, parent=parents):
        flot_courant = float("inf")

        vertex = dest
        while vertex != source:
            flot_courant = min(flot_courant, graph[parents[vertex]][vertex])
            vertex = parents[vertex]
        flot_maximum += flot_courant

        vertex = dest
        while vertex != source:
            child_vertex = parents[vertex]
            graph[child_vertex][vertex] -= flot_courant
            graph[vertex][child_vertex] += flot_courant
            vertex = parents[vertex]
    return flot_maximum
