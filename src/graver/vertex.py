class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = set()

    def outgoing_edges(self):
        for edge in self.edges:
            successor = edge.get_successor(self)
            if successor is not None:
                yield edge
