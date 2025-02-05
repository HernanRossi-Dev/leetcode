import multiprocessing
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def traverse_tree(self, node: TreeNode, depth: int) -> int:
        if not node:
            return 0
        l_depth = r_depth = depth
        if node.left:
            l_depth = self.traverse_tree(node.left, depth + 1)
        if node.right:
            r_depth = self.traverse_tree(node.right, depth + 1)
        return max([l_depth, r_depth])

    def find_max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = self.traverse_tree(root, 1)
        return max_depth

    def find_max_depth_multiprocess(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_node = root.left
        right_node = root.right
        with multiprocessing.Pool(2) as pool:
            results = pool.starmap(self.traverse_tree, zip([left_node, right_node], repeat(1)))
        l_depth, r_depth = results
        return max(l_depth, r_depth) + 1