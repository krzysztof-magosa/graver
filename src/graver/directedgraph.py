from graver.basegraph import BaseGraph


class DirectedGraph(BaseGraph):
    def add_edge(self, source, target, weight=1):
        parent = super(DirectedGraph, self)
        return parent._add_edge(source, target, weight=weight, oneway=True)
