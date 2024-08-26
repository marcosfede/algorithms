from typing import Dict, List, Tuple
import heapq

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Implements Dijkstra's algorithm for finding the shortest path in a graph.

    Args:
    graph (Dict[int, List[Tuple[int, int]]]): A dictionary representing the graph.
                                              Keys are nodes, values are lists of (neighbor, weight) tuples.
    start (int): The starting node.

    Returns:
    Dict[int, int]: A dictionary with nodes as keys and shortest distances from start as values.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Simple graph example
    simple_graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: []
    }

    print("Simple Graph Example:")
    start_node = 0
    shortest_paths = dijkstra(simple_graph, start_node)
    print(f"Shortest paths from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"To node {node}: {distance}")

    # More complex graph example
    complex_graph = {
        0: [(1, 4), (2, 2)],
        1: [(2, 1), (3, 5)],
        2: [(3, 8), (4, 10)],
        3: [(4, 2), (5, 6)],
        4: [(5, 3)],
        5: [(6, 1)],
        6: [(4, 4), (7, 2)],
        7: []
    }

    print("\nComplex Graph Example:")
    start_node = 0
    shortest_paths = dijkstra(complex_graph, start_node)
    print(f"Shortest paths from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"To node {node}: {distance}")
