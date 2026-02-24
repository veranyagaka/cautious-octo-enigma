1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
9        res = []
10        def dfs(node, path):
11            if not node: return
12
13            path += str(node.val)
14
15            if not node.left and not node.right: # leaf node
16                res.append(int(path, 2))
17
18            dfs(node.left, path)
19            dfs(node.right, path)
20
21
22        dfs(root, "")
23        return sum(res)
24