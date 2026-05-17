1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        
10        self.prev = None
11        self.min_diff = float('infinity')
12
13        ## do inorder traversal
14        def inorder(node):
15            if not node:
16                return
17
18            inorder(node.left)
19
20            if self.prev is not None:
21                self.min_diff = min(self.min_diff, abs(node.val - self.prev))
22
23            self.prev = node.val
24
25            inorder(node.right)
26
27        inorder(root)
28
29        return self.min_diff