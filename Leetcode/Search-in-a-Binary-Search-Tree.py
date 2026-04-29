1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        def search(node):
11
12            if not node:
13                return None
14
15            if val > node.val:
16                return search(node.right)
17
18            elif val < node.val:
19                return search(node.left)
20
21            else:
22                return node
23
24
25        return search(root)
26