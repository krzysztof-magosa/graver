from graver.basegraph import BaseGraph


class UndirectedGraph(BaseGraph):
    def add_edge(self, source, target, weight=1):
        parent = super(UndirectedGraph, self)
        return parent._add_edge(source, target, weight=weight, oneway=False)
