1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9
10        def dfs(node):
11            if not node:
12                return 0
13
14            left = dfs(node.left)
15            
16            right = dfs(node.right)
17
18            return 1 + max(left, right)
19            
20        
21
22        return dfs(root)