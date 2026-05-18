1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
9        range_sum = 0
10        
11        def traverse(node):
12            nonlocal range_sum
13            if not node:
14                return
15
16            if node.val >= low and node.val <= high:
17                range_sum += node.val
18            
19            traverse(node.left)
20            traverse(node.right)
21
22
23
24        traverse(root)
25        return range_sum