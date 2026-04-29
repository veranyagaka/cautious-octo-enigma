1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9
10        ## look for where to put it
11        ## connect pointers
12
13        new_node = TreeNode(val)
14
15        if not root:
16            return new_node
17
18        if val > root.val:
19            root.right = self.insertIntoBST(root.right, val)
20
21        else:
22            root.left = self.insertIntoBST(root.left, val)
23
24
25    
26
27        return root