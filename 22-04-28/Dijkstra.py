from queue import PriorityQueue


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.v = [i for i in range(num_vertices)]
        self.edges = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, source):
        # We will use priority queue to store all the visited nodes with dist as the priority
        pq = PriorityQueue()
        pq.put((0, source))
        # Initialize the distance to be infinite for all nodes except for source
        dist = [float('inf') for i in range(self.num_vertices)]
        dist[source] = 0

        while not pq.empty():
            (_, vertex) = pq.get()
            if vertex in self.visited:
                continue
            self.visited.append(vertex)

            for neighbor in self.v:
                if neighbor not in self.visited and self.edges[vertex][neighbor] != -1:
                    distance = self.edges[vertex][neighbor]
                    if dist[vertex] + distance < dist[neighbor]:
                        new_cost = dist[vertex] + distance
                        dist[neighbor] = new_cost
                        pq.put((new_cost, neighbor))
        return dist


# The run-time complexity is O(E + VlogV)
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)

print(g.dijkstra(0))
