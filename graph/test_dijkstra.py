import unittest
from dijkstra import Graph, dijkstra, shortest_path

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "C", 2)
        self.graph.add_edge("B", "D", 3)
        self.graph.add_edge("C", "B", 1)
        self.graph.add_edge("C", "D", 5)
        self.graph.add_edge("D", "E", 2)

    def test_shortest_path(self):
        path = shortest_path(self.graph, "A", "E")
        self.assertEqual(path, ["A", "C", "B", "D", "E"])

    def test_dijkstra_distances(self):
        distances, _ = dijkstra(self.graph, "A")
        expected_distances = {
            "A": 0,
            "B": 3,
            "C": 2,
            "D": 6,
            "E": 8
        }
        self.assertEqual(distances, expected_distances)

    def test_disconnected_graph(self):
        disconnected_graph = Graph()
        disconnected_graph.add_edge("A", "B", 1)
        disconnected_graph.add_edge("C", "D", 1)

        path = shortest_path(disconnected_graph, "A", "D")
        self.assertEqual(path, [])

    def test_single_node_path(self):
        path = shortest_path(self.graph, "A", "A")
        self.assertEqual(path, ["A"])

if __name__ == '__main__':
    unittest.main()
