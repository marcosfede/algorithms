from typing import Dict, List, Tuple
import heapq

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implements Dijkstra's algorithm for finding the shortest path in a weighted graph.

    Args:
    graph (Dict[str, Dict[str, int]]): A dictionary representing the graph.
                                       Keys are node names, values are dictionaries
                                       of neighboring nodes and their distances.
    start (str): The starting node.

    Returns:
    Tuple[Dict[str, int], Dict[str, str]]: A tuple containing two dictionaries:
        1. Shortest distances from start to each node.
        2. Previous node in the optimal path from start to each node.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def get_path(previous: Dict[str, str], start: str, end: str) -> List[str]:
    """
    Reconstructs the path from start to end using the previous node dictionary.

    Args:
    previous (Dict[str, str]): Dictionary of previous nodes in the optimal path.
    start (str): The starting node.
    end (str): The ending node.

    Returns:
    List[str]: The path from start to end.
    """
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    return path[::-1]

# Example usage and test case
if __name__ == "__main__":
    # Example graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }

    start_node = 'A'
    end_node = 'F'

    distances, previous = dijkstra(graph, start_node)
    path = get_path(previous, start_node, end_node)

    print(f"Shortest distances from {start_node}: {distances}")
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}")
    print(f"Total distance: {distances[end_node]}")

# Test cases
def test_dijkstra():
    # Test case 1: Simple graph
    graph1 = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    distances1, previous1 = dijkstra(graph1, 'A')
    assert distances1 == {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    assert get_path(previous1, 'A', 'D') == ['A', 'B', 'C', 'D']

    # Test case 2: Disconnected graph
    graph2 = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 1},
        'D': {'C': 1}
    }
    distances2, previous2 = dijkstra(graph2, 'A')
    assert distances2 == {'A': 0, 'B': 1, 'C': float('infinity'), 'D': float('infinity')}

    print("All test cases passed!")

test_dijkstra()
