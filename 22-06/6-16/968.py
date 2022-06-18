# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Traverse all the way from leaf to root node, we define 3 states of nodes.
TYPE1 Camera state(node)
All the subtree of nodes are covered and a camera is installed on node
TYPE2 Cover state(node)
All the subtree of node are covered so is the node, but a camera is not installed on node
This implies at least one of the children is in Camera state.
TYPE3 Normal state(node)
All the subtree of node are covered but the the node is not cover.
This implies all children should be in Cover state.
Define:
Camera[node] as minimum number of cameras installed for node to be in camera state
Cover[node] as minimum number of cameras installed for node to be in cover state
Normal[node] as minimum number of cameras installed for node to be in normal state.
The recurrence relationship would be
Normal[node] = Cover[node.left] + Cover[node.right]
Cover[node] = min(Cover[node.left] + Camera[node.right], 
Camera[node.left] + Cover[node.right], 
Camera[node.left] + Camera[node.right) 
Camera[node] = min(Cover[node.left], Normal[node.left], Camera[node.left]) +
min (Cover[node.right], Normal[node.right], Camera[node.right]) + 1
Thus the solution of the problem will be:
min (Camera[node], Cover[node])
"""
class Solution:
    def minNodeState(self, node):
        if not node:
            return float('inf'), 0, 0
        L = self.minNodeState(node.left)
        lcamera, lcover, lnormal = L
        R = self.minNodeState(node.right)
        rcamera, rcover, rnormal = R
        normal = lcover + rcover
        cover = min(lcover + rcamera, lcamera + rcover, lcamera + rcamera)
        camera = min(L) + min(R) + 1
        return camera, cover, normal

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return min(self.minNodeState(root)[0:2])


