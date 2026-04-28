1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        ## preorder traversal
10        ## dfs approach
11        ans = []
12
13        def dfs(node):
14            if not node:
15                return
16
17            ans.append(node.val)
18
19            if node.left:
20                dfs(node.left)
21
22            if node.right:
23                dfs(node.right)
24        dfs(root)
25
26        return ans