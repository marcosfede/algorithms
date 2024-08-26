import unittest
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: [(4, 3)],
            4: []
        }
        start_node = 0
        expected = {0: 0, 1: 3, 2: 1, 3: 4, 4: 7}
        self.assertEqual(dijkstra(graph, start_node), expected)

    def test_disconnected_graph(self):
        graph = {
            0: [(1, 1)],
            1: [(0, 1)],
            2: [(3, 1)],
            3: [(2, 1)]
        }
        start_node = 0
        expected = {0: 0, 1: 1, 2: float('infinity'), 3: float('infinity')}
        self.assertEqual(dijkstra(graph, start_node), expected)

    def test_single_node_graph(self):
        graph = {0: []}
        start_node = 0
        expected = {0: 0}
        self.assertEqual(dijkstra(graph, start_node), expected)

    def test_complex_graph(self):
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(2, 1), (3, 5)],
            2: [(3, 8), (4, 10)],
            3: [(4, 2), (5, 6)],
            4: [(5, 3)],
            5: []
        }
        start_node = 0
        expected = {0: 0, 1: 4, 2: 2, 3: 9, 4: 11, 5: 14}
        self.assertEqual(dijkstra(graph, start_node), expected)

    def test_start_node_not_in_graph(self):
        graph = {0: [(1, 1)], 1: [(0, 1)]}
        start_node = 2
        with self.assertRaises(KeyError):
            dijkstra(graph, start_node)

if __name__ == '__main__':
    unittest.main()
