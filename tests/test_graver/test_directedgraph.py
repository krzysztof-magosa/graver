import unittest
from graver import DirectedGraph
from graver import shortest_path


class TestDirectedGraph(unittest.TestCase):
    def test_shortest_path(self):
        g = DirectedGraph()
        a = g.add_vertex('a')
        b = g.add_vertex('b')
        c = g.add_vertex('c')

        g.add_edge('b', 'a', weight=1)
        g.add_edge('c', 'b', weight=2)

        # This edge should NOT be used for c->a
        # because it has opposite direction
        g.add_edge('a', 'c', weight=1)

        route = shortest_path(g, 'c', 'a')

        self.assertEqual([c, b, a], route[0])
        self.assertEqual(3, route[1])


if __name__ == '__main__':
    unittest.main()
