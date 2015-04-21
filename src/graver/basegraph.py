from graver.edge import Edge
from graver.vertex import Vertex


class BaseGraph(object):
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def find_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            assert(vertex in self.vertices)
            return vertex
        else:
            return self.get_vertex(vertex)

    def get_vertex(self, id):
        for item in self.vertices:
            if item.id == id:
                return item

        raise IndexError("Vertex not found in graph")
        
    def add_vertex(self, id):
        vertex = Vertex(id)
        self.vertices.add(vertex)
        return vertex

    def _add_edge(self, source, target, weight=1, oneway=False):
        source = self.find_vertex(source)
        target = self.find_vertex(target)

        edge = Edge(source, target, weight=weight, oneway=oneway)
        self.edges.add(edge)
        return edge
