use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

// Define the Graph structure
struct Graph {
    edges: HashMap<usize, Vec<(usize, usize)>>,
}

// Define the Node structure for the priority queue
#[derive(Copy, Clone, Eq, PartialEq)]
struct Node {
    cost: usize,
    vertex: usize,
}

// Implement Ord and PartialOrd for Node to use in BinaryHeap
impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Graph {
    // Constructor for Graph
    fn new() -> Self {
        Graph {
            edges: HashMap::new(),
        }
    }

    // Method to add an edge to the graph
    fn add_edge(&mut self, from: usize, to: usize, cost: usize) {
        self.edges.entry(from).or_insert(Vec::new()).push((to, cost));
        self.edges.entry(to).or_insert(Vec::new()); // Ensure all vertices are in the map
    }

    // Dijkstra's algorithm to find the shortest path
    fn dijkstra(&self, start: usize, end: usize) -> Option<(Vec<usize>, usize)> {
        let mut distances: HashMap<usize, usize> = HashMap::new();
        let mut heap = BinaryHeap::new();
        let mut predecessors: HashMap<usize, usize> = HashMap::new();

        // Initialize distances
        for &vertex in self.edges.keys() {
            distances.insert(vertex, std::usize::MAX);
        }
        distances.insert(start, 0);
        heap.push(Node { cost: 0, vertex: start });

        while let Some(Node { cost, vertex }) = heap.pop() {
            if vertex == end {
                let mut path = vec![end];
                let mut current = end;
                while let Some(&pred) = predecessors.get(&current) {
                    path.push(pred);
                    current = pred;
                }
                path.reverse();
                return Some((path, cost));
            }

            if cost > distances[&vertex] {
                continue;
            }

            if let Some(neighbors) = self.edges.get(&vertex) {
                for &(neighbor, edge_cost) in neighbors {
                    let new_cost = cost + edge_cost;
                    if new_cost < distances[&neighbor] {
                        distances.insert(neighbor, new_cost);
                        predecessors.insert(neighbor, vertex);
                        heap.push(Node { cost: new_cost, vertex: neighbor });
                    }
                }
            }
        }

        None // No path found
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simple_path() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 4);
        graph.add_edge(1, 2, 3);
        graph.add_edge(2, 3, 2);

        let result = graph.dijkstra(0, 3);
        assert_eq!(result, Some((vec![0, 1, 2, 3], 9)));
    }

    #[test]
    fn test_multiple_paths() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 4);
        graph.add_edge(0, 2, 1);
        graph.add_edge(1, 3, 1);
        graph.add_edge(2, 1, 2);
        graph.add_edge(2, 3, 5);

        let result = graph.dijkstra(0, 3);
        assert_eq!(result, Some((vec![0, 2, 1, 3], 4)));
    }

    #[test]
    fn test_no_path() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 4);
        graph.add_edge(1, 2, 3);
        graph.add_edge(3, 4, 2);

        let result = graph.dijkstra(0, 4);
        assert_eq!(result, None);
    }

    #[test]
    fn test_graph_with_cycle() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 1);
        graph.add_edge(1, 2, 2);
        graph.add_edge(2, 3, 3);
        graph.add_edge(3, 1, 1);
        graph.add_edge(3, 4, 4);

        let result = graph.dijkstra(0, 4);
        assert_eq!(result, Some((vec![0, 1, 2, 3, 4], 10)));
    }

    #[test]
    fn test_large_graph() {
        let mut graph = Graph::new();
        for i in 0..1000 {
            graph.add_edge(i, i + 1, 1);
        }
        graph.add_edge(0, 1000, 999);

        let result = graph.dijkstra(0, 1000);
        assert_eq!(result, Some((vec![0, 1000], 999)));
    }
}
