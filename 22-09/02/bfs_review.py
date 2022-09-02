# Key insight of BFS:
# 1. We can use a queue to store the nodes we need to visit. The order of the queue is the depth
# of the node from the source
# 2. We can use a set to store the nodes we have visited. Visited nodes are essential for graph to avoid cycles.
# 3. We can append additional information to the queue, such as the path, the depth, and the parent node.
# 4. Traversing the tree is a special case of the graph, where we don't need to keep track of visited nodes.


# Time complexity: O(V + E)
# Space complexity: O(V)


G = {'A': ['B', 'C'],
     'B': ['A', 'C', 'D'],
     'C': ['A', 'B', 'D', 'E'],
     'D': ['B', 'C', 'E', 'F'],
     'E': ['C', 'D', 'F'],
     'F': ['D', 'E']}


def bfs_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == end:
                return path
            else:
                for neigh in graph[vertex]:
                    queue.append((neigh, path + [neigh]))
    return None


def bfs_traverse(graph, start):
    queue = [(start, 0)]
    visited = set(start)
    while queue:
        node, depth = queue.pop(0)
        print(node, depth)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                visited.add(neighbor)


def bfs_full(graph):
    queue = []
    visited = set()
    for node in graph:
        if node not in visited:
            print(node, "discovered")
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.pop(0)
                print(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)


# Create a disconnected graph example
G_dis = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'E'],
         'D': ['B', 'C', 'E', 'F'],
         'E': ['C', 'D', 'F'],
         'F': ['D', 'E'],
         'G': ['H', 'I'],
         'H': ['G', 'I'],
         'I': ['G', 'H']}


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Define a binary tree instance
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
root.right.right.right = Node(7)
root.right.right.right.left = Node(8)
root.right.right.right.left.left = Node(9)
root.right.right.right.left.right = Node(10)
root.right.right.right.left.right.left = Node(11)
root.right.right.right.left.right.right = Node(12)
root.right.right.right.left.right.right.left = Node(13)
root.right.right.right.left.right.right.right = Node(14)
root.right.right.right.left.right.right.right = Node(14)


def bfs_tree(tree):
    queue = [(tree, 0)]
    while queue:
        node, depth = queue.pop(0)
        print(node.val, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))


if __name__ == "__main__":
    print("BFS path from A to F:", bfs_path(G, 'A', 'F'))
    print("BFS graph traversal from A :")
    bfs_traverse(G, 'A')
    print("BFS tree traversal:")
    bfs_tree(root)
    print("BFS full traversal for disconnected graph:")
    bfs_full(G_dis)
