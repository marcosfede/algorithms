"""
Dijkstra's algorithm for finding the shortest path between nodes in a graph.

Real-life scenario: Finding the shortest route between two locations on a map,
where nodes represent locations and edges represent roads with their distances.
"""

from typing import Dict, List, Tuple
import heapq


class Graph:
    def __init__(self):
        self.nodes: Dict[str, Dict[str, int]] = {}

    def add_edge(self, from_node: str, to_node: str, distance: int):
        if from_node not in self.nodes:
            self.nodes[from_node] = {}
        self.nodes[from_node][to_node] = distance

    def get_neighbors(self, node: str) -> Dict[str, int]:
        return self.nodes.get(node, {})


def dijkstra(graph: Graph, start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implements Dijkstra's algorithm for finding the shortest path in a weighted graph.

    Args:
    graph (Graph): A Graph object representing the graph.
    start (str): The starting node.

    Returns:
    Tuple[Dict[str, int], Dict[str, str]]: A tuple containing two dictionaries:
        1. Shortest distances from start to each node.
        2. Previous node in the optimal path from start to each node.
    """
    distances: Dict[str, int] = {start: 0}
    previous_nodes: Dict[str, str] = {}
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances.get(current_node, float('inf')):
            continue

        for neighbor, weight in graph.get_neighbors(current_node).items():
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes


def shortest_path(graph: Graph, start: str, end: str) -> List[str]:
    """
    Finds the shortest path between start and end nodes in the graph.

    Args:
    graph (Graph): A Graph object representing the graph.
    start (str): The starting node.
    end (str): The ending node.

    Returns:
    List[str]: The shortest path from start to end.
    """
    distances, previous_nodes = dijkstra(graph, start)

    if end not in distances:
        return []

    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.append(start)

    return list(reversed(path))


# Example usage and test case
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 3)
    g.add_edge("C", "B", 1)
    g.add_edge("C", "D", 5)
    g.add_edge("D", "E", 2)

    # Find shortest path from A to E
    path = shortest_path(g, "A", "E")
    print(f"Shortest path from A to E: {' -> '.join(path)}")

    # Find distances from A to all other nodes
    distances, _ = dijkstra(g, "A")
    for node, distance in distances.items():
        print(f"Shortest distance from A to {node}: {distance}")

    # Test cases
    def test_dijkstra():
        # Test case 1: Simple graph
        g1 = Graph()
        g1.add_edge("A", "B", 1)
        g1.add_edge("A", "C", 4)
        g1.add_edge("B", "C", 2)
        g1.add_edge("B", "D", 5)
        g1.add_edge("C", "D", 1)

        distances1, previous1 = dijkstra(g1, "A")
        assert distances1 == {"A": 0, "B": 1, "C": 3, "D": 4}
        assert shortest_path(g1, "A", "D") == ["A", "B", "C", "D"]

        # Test case 2: Disconnected graph
        g2 = Graph()
        g2.add_edge("A", "B", 1)
        g2.add_edge("C", "D", 1)

        distances2, _ = dijkstra(g2, "A")
        assert distances2 == {"A": 0, "B": 1}
        assert shortest_path(g2, "A", "D") == []

        print("All test cases passed!")

    test_dijkstra()
