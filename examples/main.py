#! /usr/bin/env python

from graver import DirectedGraph
from graver import shortest_path


if __name__ == "__main__":
    graph = DirectedGraph()

    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')

    graph.add_edge('a', 'b', weight=5)
    graph.add_edge('b', 'c', weight=5)
    graph.add_edge('a', 'c', weight=7)
    graph.add_edge('c', 'a', weight=1)

    route = shortest_path(graph, 'c', 'a')
    print([x.id for x in route[0]])
    print(route[1])
