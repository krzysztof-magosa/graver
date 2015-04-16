import unittest
from graver import UndirectedGraph
from graver import shortest_path


class TestDirectedGraph(unittest.TestCase):
    def test_shortest_path(self):
        g = UndirectedGraph()
        a = g.add_vertex('a')
        b = g.add_vertex('b')
        c = g.add_vertex('c')

        g.add_edge('a', 'b', weight=1)
        g.add_edge('b', 'c', weight=2)
        g.add_edge('a', 'c', weight=1)

        route = shortest_path(g, 'c', 'a')

        self.assertEqual([c, a], route[0])
        self.assertEqual(1, route[1])


if __name__ == '__main__':
    unittest.main()
