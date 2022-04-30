# https://leetcode.com/problems/evaluate-division/
from typing import List


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # Let us first convert the equations into the weighted edge using adjacency matrix representation
    nodes = list(set(item for equation in equations for item in equation))
    n = len(nodes)
    node_map = {}
    for i in range(n):
        node_map[nodes[i]] = i
    adj_matrix = [[0] * n for i in range(n)]
    for i in range(len(equations)):
        node1, node2 = node_map[equations[i][0]], node_map[equations[i][1]]
        adj_matrix[node1][node2] = values[i]
        adj_matrix[node2][node1] = 1 / values[i]
    answer = [-1] * len(queries)

    # Since we assume there is no conflict between nodes, all the accumulated path products from node i to j are the
    # same. We can stop immediately when we find an answer. We use a modified BFS to keep track of the quotient from
    # source to node j and return immediately when arrives at the destination
    def BFS(source, dest):
        dist = [-1] * n
        queue = [source]
        dist[source] = 1
        visited = [source]
        while queue:
            node = queue.pop(0)
            node_dist = dist[node]
            for neigh, weight in enumerate(adj_matrix[node]):
                if weight != 0 and neigh not in visited:
                    queue.append(neigh)
                    visited.append(neigh)
                    dist[neigh] = node_dist * weight
                    if dest == neigh:
                        answer[idx] = dist[neigh]
                        return

    for idx, query in enumerate(queries):
        if query[0] not in nodes or query[1] not in nodes:
            answer[idx] = -1
            continue
        if query[0] == query[1]:
            answer[idx] = 1
            continue
        src, det = node_map[query[0]], node_map[query[1]]
        BFS(src, det)
    return answer


print(calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "a"]]))
print(calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                   [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
print(calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
