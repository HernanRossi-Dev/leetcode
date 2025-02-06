from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvertBinaryTree:
    def traverse_node_and_swap_children(self, node: TreeNode) -> None:
        t_left = node.left
        node.left = node.right
        node.right = t_left
        if node.left:
            self.traverse_node_and_swap_children(node.left)
        if node.right:
            self.traverse_node_and_swap_children(node.right)

    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # go through each node in the tree and swap the left child pointer with the right child pointer
        self.traverse_node_and_swap_children(root)
        return root
