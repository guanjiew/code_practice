# https://leetcode.com/problems/is-graph-bipartite/
# Some resource about Bipartite graph:
# https://www.baeldung.com/cs/graphs-bipartite We need to consider the case where the graph is not fully connected.
# Some important properties about bipartite graphs:
# A graph is a bipartite graph iff it does not contain odd cycles and iff it is 2-colorable
# We use the 2-colorable property and traverse with BFS to find if the graph is 2-colorable in the solution
# In such case, we need to try out the other uncolored node as the source of BFS as they are disconnected from the
# rest of the graph.
# Run-time complexity should be O(V+E)
# Another possible solution is using the max flow algorithm,
# check this video https://www.youtube.com/watch?v=GhjwOiJ4SqU&t=378s for graphical explanatory
from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    colors = [None] * n
    for source in range(n):
        if graph[source] and colors[source] is None:
            colors[source] = False
            queue = [source]
            while queue:
                node = queue.pop(0)
                color = colors[node]
                for neigh in graph[node]:
                    if colors[neigh] is None:
                        colors[neigh] = not color
                        queue.append(neigh)
                    elif colors[neigh] == color:
                        return False
    return True


graph1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(graph1))
