class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = set()

    def edges_from(self, vertex):
        for edge in self.edges:
            successor = edge.get_successor(vertex)
            if successor is not None:
                yield edge
