use std::collections::{HashMap, VecDeque};
use rand::Rng;

// Adaptive Edge Exploration (AEE) Algorithm
//
// This algorithm explores a graph by adaptively choosing edges based on their
// weights and the graph's structure. It aims to find paths that balance between
// shortest distance and interesting graph features, introducing some randomness
// to explore diverse paths.

// Define the Graph structure
struct Graph {
    edges: HashMap<usize, Vec<(usize, usize)>>,
}

// Define the Node structure for the exploration queue
#[derive(Clone, Eq, PartialEq)]
struct Node {
    vertex: usize,
    path: Vec<usize>,
    total_cost: usize,
    interest_score: f64,
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

    // Adaptive Edge Exploration (AEE) algorithm
    fn adaptive_edge_exploration(&self, start: usize, end: usize) -> Option<(Vec<usize>, usize)> {
        let mut rng = rand::thread_rng();
        let mut queue = VecDeque::new();
        let mut visited = HashMap::new();

        queue.push_back(Node {
            vertex: start,
            path: vec![start],
            total_cost: 0,
            interest_score: 0.0,
        });

        while let Some(current) = queue.pop_front() {
            if current.vertex == end {
                return Some((current.path, current.total_cost));
            }

            if let Some(&prev_cost) = visited.get(&current.vertex) {
                if current.total_cost >= prev_cost {
                    continue;
                }
            }

            visited.insert(current.vertex, current.total_cost);

            if let Some(neighbors) = self.edges.get(&current.vertex) {
                let mut adaptive_neighbors = neighbors.clone();
                adaptive_neighbors.sort_by(|a, b| {
                    let a_score = self.calculate_interest_score(a.0, &current);
                    let b_score = self.calculate_interest_score(b.0, &current);
                    b_score.partial_cmp(&a_score).unwrap()
                });

                for &(neighbor, edge_cost) in adaptive_neighbors.iter() {
                    if !visited.contains_key(&neighbor) || current.total_cost + edge_cost < visited[&neighbor] {
                        let mut new_path = current.path.clone();
                        new_path.push(neighbor);
                        let new_interest_score = self.calculate_interest_score(neighbor, &current);

                        queue.push_back(Node {
                            vertex: neighbor,
                            path: new_path,
                            total_cost: current.total_cost + edge_cost,
                            interest_score: new_interest_score,
                        });
                    }
                }
            }

            // Introduce some randomness to explore different paths
            if rng.gen::<f64>() < 0.1 {
                queue.make_contiguous().shuffle(&mut rng);
            }
        }

        None // No path found
    }

    // Calculate interest score for a neighbor
    fn calculate_interest_score(&self, neighbor: usize, current: &Node) -> f64 {
        let neighbor_degree = self.edges.get(&neighbor).map_or(0, |edges| edges.len());
        let path_length = current.path.len() as f64;
        let total_cost = current.total_cost as f64;

        // Combine factors to create an interest score
        (neighbor_degree as f64).sqrt() + (1.0 / (path_length + 1.0)) + (1.0 / (total_cost + 1.0))
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

        let result = graph.adaptive_edge_exploration(0, 3);
        assert!(result.is_some());
        let (path, cost) = result.unwrap();
        assert_eq!(path, vec![0, 1, 2, 3]);
        assert_eq!(cost, 9);
    }

    #[test]
    fn test_multiple_paths() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 4);
        graph.add_edge(0, 2, 1);
        graph.add_edge(1, 3, 1);
        graph.add_edge(2, 1, 2);
        graph.add_edge(2, 3, 5);

        let result = graph.adaptive_edge_exploration(0, 3);
        assert!(result.is_some());
        let (path, cost) = result.unwrap();
        assert!(path.starts_with(&[0]) && path.ends_with(&[3]));
        assert!(cost <= 6); // The cost should be at most 6 (0->2->1->3 or 0->1->3)
    }

    #[test]
    fn test_no_path() {
        let mut graph = Graph::new();
        graph.add_edge(0, 1, 4);
        graph.add_edge(1, 2, 3);
        graph.add_edge(3, 4, 2);

        let result = graph.adaptive_edge_exploration(0, 4);
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

        let result = graph.adaptive_edge_exploration(0, 4);
        assert!(result.is_some());
        let (path, cost) = result.unwrap();
        assert!(path.starts_with(&[0]) && path.ends_with(&[4]));
        assert!(cost <= 10); // The cost should be at most 10 (0->1->2->3->4)
    }

    #[test]
    fn test_large_graph() {
        let mut graph = Graph::new();
        for i in 0..1000 {
            graph.add_edge(i, i + 1, 1);
        }
        graph.add_edge(0, 1000, 999);

        let result = graph.adaptive_edge_exploration(0, 1000);
        assert!(result.is_some());
        let (path, cost) = result.unwrap();
        assert!(path.starts_with(&[0]) && path.ends_with(&[1000]));
        assert!(cost <= 999); // The cost should be at most 999 (direct path from 0 to 1000)
    }
}
