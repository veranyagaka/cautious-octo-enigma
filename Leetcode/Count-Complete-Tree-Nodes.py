1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countNodes(self, root: Optional[TreeNode]) -> int:
9        ## less than o(n) TC
10
11        ## brute force first
12        if not root: return 0
13
14        left = self.countNodes(root.left)
15        right = self.countNodes(root.right)
16
17        return 1 + left + right 