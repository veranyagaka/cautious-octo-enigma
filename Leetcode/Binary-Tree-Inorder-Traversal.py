1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        ans = []
11        def traverse(node):
12            if node is None:
13                return
14            traverse(node.left)
15            ans.append(node.val)
16            traverse(node.right)
17        
18        traverse(root)
19        return ans
20