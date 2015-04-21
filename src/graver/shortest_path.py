from graver import PriorityQueue
from math import isinf


def extract_path(previous, target):
    path = []
    elem = target
    while True:
        path.insert(0, elem)

        if elem not in previous:
            break

        elem = previous[elem]

    return path


def shortest_path(graph, source, target):
    source = graph.find_vertex(source)
    target = graph.find_vertex(target)

    distances = {k: float('inf') for k in graph.vertices if k != source}
    distances[source] = 0

    previous = {}

    pq = PriorityQueue()
    for vertex in graph.vertices:
        pq.push(vertex, distances[vertex])

    while pq:
        closest = pq.pop()

        if closest == target:
            break

        for edge in closest.outgoing_edges():
            # edge is not added to this graph
            if edge not in graph.edges:
                continue

            neigh = edge.get_successor(closest)

            # no successor, e.g. oneway edge
#            if neigh is None:
#                continue

            # already visited
            if neigh not in pq:
                continue

            if isinf(distances[closest]):
                alt = edge.weight
            else:
                alt = distances[closest] + edge.weight

            if alt < distances[neigh]:
                distances[neigh] = alt
                previous[neigh] = closest

                pq.push(neigh, alt)

    path = extract_path(previous, target)

    if source not in path or target not in path:
        raise IndexError("Cannot find path")

    return (path, distances[target])
