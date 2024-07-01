import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        # Priority queue to store (distance, vertex) pairs
        heap = [(0, start)]
        # Dictionary to store the shortest path to each vertex
        shortest_paths = {start: (None, 0)}
        # Set of visited nodes
        visited = set()

        while heap:
            (current_distance, current_vertex) = heapq.heappop(heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight
                if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                    shortest_paths[neighbor] = (current_vertex, distance)
                    heapq.heappush(heap, (distance, neighbor))

        return shortest_paths

def print_shortest_paths(shortest_paths, start):
    print(f"Shortest paths from vertex {start}:")
    for vertex, (predecessor, distance) in shortest_paths.items():
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = shortest_paths[vertex][0]
        path.reverse()
        print(f"Distance to {path[-1]}: {shortest_paths[path[-1]][1]}, Path: {' -> '.join(map(str, path))}")

# Test
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = graph.dijkstra(start_vertex)
    print_shortest_paths(shortest_paths, start_vertex)
