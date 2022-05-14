import heapq


# Dijkstra algorithm divides all the nodes into explored and unexplored.
# For nodes in explored, the value found is the shortest distance from source
# It will explore the shortest unexplored node and update the distance if a shorter one is found
# It works for single source problem with non-negative edges
# Pres-duo Code
# def Dijkstra(source, destination):
#     for each vertex v
#         dist [v] = inf
#         prev [v] = None
#     dist[source] = 0
#     explored = []
#     set unexplored as priority queue
#     while destination not in explored:
#         v <- unexplored.pop()
#         set v to be explored
#         for all edges in (v, w):
#             if dist[v] + cost(v, w) < dist(w):
#                 dist(w) = dist(v) + cost(v, w)
#                 prev[w] = v
#     return dist[destination]
#


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.v = [i for i in range(num_vertices)]
        self.edges = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visited = []
        self.unexplored = []
        self.dist = [float('inf') for i in range(self.num_vertices)]

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, source):
        heapq.heappush(self.unexplored, (0, source))
        self.dist[source] = 0
        self.visited.append(source)

        while self.unexplored:
            (_, vertex) = heapq.heappop(self.unexplored)
            self.visited.append(vertex)
            for neighbor in self.v:
                if neighbor not in self.visited and self.edges[vertex][neighbor] != -1:
                    distance = self.edges[vertex][neighbor]
                    if self.dist[vertex] + distance < self.dist[neighbor]:
                        new_cost = self.dist[vertex] + distance
                        self.dist[neighbor] = new_cost
                        heapq.heappush(self.unexplored, (new_cost, neighbor))
        return self.dist


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
