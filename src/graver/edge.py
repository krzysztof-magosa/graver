class Edge:
    def __init__(self, source, target, weight=1, oneway=False):
        self.source = source
        self.target = target
        self.weight = weight
        self.oneway = oneway

        self.source.edges.add(self)
        self.target.edges.add(self)

    def get_successor(self, opposite=None):
        vertices = set([self.target])

        if not self.oneway:
            vertices.add(self.source)

        if opposite is not None and opposite in vertices:
            vertices.remove(opposite)

        return vertices.pop() if len(vertices) else None
