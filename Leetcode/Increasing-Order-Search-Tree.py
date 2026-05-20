1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        """
10        build a new tree
11        """
12
13        ## inorder traversal
14        def traverse(node, curr):
15            if not node:
16                return curr
17
18
19            curr = traverse(node.left, curr)
20            node.left = None
21            curr.right = node
22            curr = node
23            curr = traverse(node.right, curr)
24
25            return curr
26
27        dummy = TreeNode(0)
28        curr = dummy
29        traverse(root, curr)
30
31        return dummy.right